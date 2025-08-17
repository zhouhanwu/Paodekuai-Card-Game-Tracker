import streamlit as st
import pandas as pd
from translations import get_text

# ---------------------
# 1. App Configuration
# ---------------------
st.set_page_config(
    page_title="Paodekuai Game Tracker - 跑得快游戏追踪器",
    layout="wide"  # Gives us space for the right-hand panel
)

# ---------------------
# 2. Initialize Session State
# ---------------------
if "players" not in st.session_state:
    st.session_state.players = []
if "sets" not in st.session_state:
    st.session_state.sets = []  # List of DataFrames for each set
if "payments" not in st.session_state:
    st.session_state.payments = []  # Money transactions per set
if "show_fu_toast" not in st.session_state:
    st.session_state.show_fu_toast = False  # Control for FU toast notification
if "language" not in st.session_state:
    st.session_state.language = "en"  # Default language

# ---------------------
# 3. Language Selector
# ---------------------
st.sidebar.markdown("---")
st.sidebar.markdown("**" + get_text(st.session_state.language, "language_selector") + "**")
lang = st.sidebar.selectbox(
    "Select Language / 选择语言",
    ["English", "中文"],
    index=0 if st.session_state.language == "en" else 1,
    label_visibility="collapsed"
)

# Update language in session state
if lang == "English":
    st.session_state.language = "en"
else:
    st.session_state.language = "zh"

# ---------------------
# 4. Input Form for New Session
# ---------------------
st.sidebar.header(get_text(st.session_state.language, "game_setup"))
num_players = st.sidebar.number_input(get_text(st.session_state.language, "num_players"), min_value=2, max_value=10, value=4)
player_names = []
for i in range(num_players):
    name = st.sidebar.text_input(get_text(st.session_state.language, "player_name", num=i+1), key=f"player_{i+1}") # Unique key for each player input stored in st.session_state
    player_names.append(name)

if st.sidebar.button(get_text(st.session_state.language, "start_new_game")):
    if any(name.strip() == "" for name in player_names):
        st.sidebar.warning(get_text(st.session_state.language, "warning_enter_names"))
    elif any(
        player_names[i].strip().lower() == player_names[j].strip().lower()
        for i in range(num_players) for j in range(i + 1, num_players)
    ):
        st.sidebar.warning(get_text(st.session_state.language, "warning_unique_names"))
    else:
        st.session_state.players = player_names
        st.session_state.sets = []
        st.session_state.payments = []
        st.session_state.bet_amount = []
        st.session_state.threshold = []
        st.session_state.starting_cards = []

# ---------------------
# 5. Main Game Area
# ---------------------

# Handle Fu toast after rerun
if st.session_state.show_fu_toast:
    fu_placeholder = st.empty()
    fu_placeholder.markdown(
        f"""
        <!-- autoplay audio from GitHub -->
        <audio autoplay>
            <source src="https://zhouhanwu.github.io/Paodekuai-Card-Game-Tracker/wocao.mp3" type="audio/mp3">
        </audio>
        <style>
        #fu-toast {{
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            z-index: 9999;
            background: rgba(255,255,255,0.95);
            padding: 40px 80px;
            border-radius: 20px;
            box-shadow: 0 0 40px #ff0000;
            text-align: center;
        }}
        </style>
        <div id="fu-toast">
            <span style='color:red;font-size:100px;font-weight:bold;'>
                {get_text(st.session_state.language, "fu_toast")}
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.session_state.show_fu_toast = False

    # Clear the toast after 1.5 seconds
    import time
    time.sleep(2.0)
    fu_placeholder.empty()

# Place export button to the right of the title
title_col, export_col = st.columns([5, 1])
with title_col:
    st.title(get_text(st.session_state.language, "main_title"))
    st.markdown(get_text(st.session_state.language, "main_description"))
with export_col:
    st.markdown("\n")
    if st.button(get_text(st.session_state.language, "export_to_csv")):
        # Export sets data
        sets_csv = ""
        sets_csv += "Game Statistics\n"
        for i, df in enumerate(st.session_state.sets):
            if not df.empty:
                sets_csv += f"Set {i+1}\n"
                if not st.session_state.payments[i].empty:
                    payments_dict = st.session_state.payments[i].iloc[0].to_dict()
                    # Format each payment value to 2 decimal places
                    payments_dict = {k: f"{v:.2f}" for k, v in payments_dict.items()}
                    payments_data = {"Rounds": "Payment ($)", **payments_dict}
                    payments_df = pd.DataFrame([payments_data])
                    df_combined = pd.concat([df, payments_df], ignore_index=True)
                sets_csv += df_combined.to_csv(index=False)
                sets_csv += "\n\n"
        st.download_button(
            label=get_text(st.session_state.language, "download_csv"),
            data=sets_csv,
            file_name="paodekuai_export.csv",
            mime="text/csv"
        )

st.markdown("---")

if not st.session_state.players:
    st.info(get_text(st.session_state.language, "please_start_game"))
else:
    # Display previous sets
    for set_index, df in enumerate(st.session_state.sets):
        col1, col2 = st.columns([3, 1])  # Wider left, smaller right

        with col1:
            # Header and delete button on the same line
            header_col, delete_col = st.columns([4,1])
            with header_col:
                st.subheader(get_text(st.session_state.language, "set", num=set_index+1))
            with delete_col:
                if not st.session_state.sets[0].empty:
                    if st.button(get_text(st.session_state.language, "delete"), key=f"delete_button_{set_index}"):
                        del st.session_state.sets[set_index]
                        if set_index < len(st.session_state.payments):
                            del st.session_state.payments[set_index]
                        if set_index < len(st.session_state.bet_amount):
                            del st.session_state.bet_amount[set_index]
                        if set_index < len(st.session_state.threshold):
                            del st.session_state.threshold[set_index]
                        if set_index < len(st.session_state.starting_cards):
                            del st.session_state.starting_cards[set_index]
                        st.rerun()

            st.markdown(get_text(st.session_state.language, "bet_amount", amount=st.session_state.bet_amount[set_index]))
            st.markdown(get_text(st.session_state.language, "elimination_threshold", threshold=st.session_state.threshold[set_index]))
            st.markdown(get_text(st.session_state.language, "starting_cards", cards=st.session_state.starting_cards[set_index]))
            
            # Highlight FU values in the DataFrame
            def highlight_fu(row):
                fu_value = st.session_state.starting_cards[set_index]
                styles = []
                # Check if this is the last row
                is_last_row = row.name == df.index[-1]
                for col in df.columns:
                    # Only highlight if not first column and not last row
                    if col != "Rounds" and not is_last_row and row[col] == fu_value:
                        styles.append("background-color: #ffeb3b")
                    else:
                        styles.append("")
                return styles

            styled_df = df.style.apply(highlight_fu, axis=1)
            st.dataframe(styled_df, hide_index=True)

        with col2:
            st.markdown(get_text(st.session_state.language, "payments_for_set", num=set_index+1))
            if set_index < len(st.session_state.payments):
                payment = st.session_state.payments[set_index]
                for player, amount in payment.iloc[0].items():
                    st.markdown(f"- {player}: ${amount:.2f}")

        st.markdown("---")

    # ---------------------
    # If set has concluded
    # ---------------------
    if len(st.session_state.sets) == len(st.session_state.payments):
        with st.form("new_set_form"):
            st.subheader(get_text(st.session_state.language, "add_new_set"))
            # Configure input fields for new set
            # Use the last submitted values if they exist, otherwise use defaults
            last_bet = st.session_state.bet_amount[-1] if st.session_state.bet_amount else 10
            last_threshold = st.session_state.threshold[-1] if st.session_state.threshold else 20
            last_cards = st.session_state.starting_cards[-1] if st.session_state.starting_cards else 13
            
            bet_amount = st.number_input(get_text(st.session_state.language, "bet_amount_per_set"), min_value=1, value=last_bet)
            threshold = st.number_input(get_text(st.session_state.language, "elimination_threshold_cards"), min_value=1, value=last_threshold)
            starting_cards = st.number_input(get_text(st.session_state.language, "starting_cards_per_player"), min_value=1, max_value=54, value=last_cards)
            submit_button = st.form_submit_button(get_text(st.session_state.language, "add"))

        # If the form is submitted, re-render page to show new set
        if submit_button:
            st.session_state.bet_amount.append(bet_amount)
            st.session_state.threshold.append(threshold)
            st.session_state.starting_cards.append(starting_cards)
            df = pd.DataFrame(columns=["Rounds"] + st.session_state.players)
            st.session_state.sets.append(df)
            st.rerun()

    # ---------------------
    # If set has yet to conclude
    # ---------------------
    if len(st.session_state.sets) > len(st.session_state.payments):
        st.subheader(get_text(st.session_state.language, "set_round", set_num=len(st.session_state.sets), round_num=st.session_state.sets[-1].shape[0] + 1))
        # Create a round input form and store in dict new_set_data
        new_set_data = {}
        for player in st.session_state.players:
            key = f"cards_remaining_{player}_{len(st.session_state.sets)-1}"
            new_set_data[player] = st.number_input(get_text(st.session_state.language, "cards_remaining", player=player),
                                                min_value=0, max_value=54, value=0, key=key)

        # On submission add to current set DataFrame
        if st.button(get_text(st.session_state.language, "add_round")):
            # Only 1 player can have 0 cards remaining, if multiple players have 0 cards, show warning
            null_card_players = []
            exceeded_card_players = []
            set_losers_fu = []
            for player, cards in new_set_data.items():
                if cards == 0:
                    null_card_players.append(player)
                elif cards == st.session_state.starting_cards[-1]:
                    set_losers_fu.append(player)
                elif cards > st.session_state.starting_cards[-1]:
                    exceeded_card_players.append(player)
                
            if len(null_card_players) > 1:
                st.warning(get_text(st.session_state.language, "warning_one_winner"))
            elif len(null_card_players) == 0:
                st.warning(get_text(st.session_state.language, "warning_need_winner"))
            elif len(exceeded_card_players) > 0:
                st.warning(get_text(st.session_state.language, "warning_exceeded_cards", players=', '.join(exceeded_card_players)))
            else:
                # Get the next round number (current number of rows + 1)
                next_round = st.session_state.sets[-1].shape[0] + 1
                # Add the round number to the new_set_data
                new_set_data_with_round = {"Rounds": next_round, **new_set_data}
                # Create DataFrame for the new round
                new_round_df = pd.DataFrame([new_set_data_with_round])
                # Concatenate to the current set
                st.session_state.sets[-1] = pd.concat([st.session_state.sets[-1], new_round_df], ignore_index=True)

                # Popup for FU
                if len(set_losers_fu) > 0:
                    st.session_state.show_fu_toast = True

                # Calculate whether any player has been eliminated, including FU
                set_losers_normal = []
                set_winners = []
                # Create pandas Series with the last set's totals
                player_totals = st.session_state.sets[-1].drop(columns=["Rounds"]).sum()
                # Add players who have been eliminated normally (mutually exclusive with FU) from the series
                for player, total in player_totals.items():
                    if total >= st.session_state.threshold[-1] and player not in set_losers_fu:
                        set_losers_normal.append(player)
                # Find out winner if any player has been eliminated
                if len(set_losers_normal) > 0 or len(set_losers_fu) > 0:
                    df_total = pd.DataFrame([{"Rounds": "Total", **player_totals}])
                    st.session_state.sets[-1] = pd.concat([st.session_state.sets[-1], df_total], ignore_index=True) # Add a total row for display
                    
                    # If FU losers are players with min cards simultaenously, we need to exclude them from the winners
                    player_totals_copy = player_totals.copy()
                    while True:
                        minimum_cards = player_totals_copy.min()
                        found_contradiction = False
                        for player, total in player_totals_copy.items():
                            if total == minimum_cards:
                                if player in set_losers_fu:
                                    player_totals_copy = player_totals_copy.drop(player)
                                    found_contradiction = True
                                    break  # Restart the loop with new minimum
                                else:
                                    set_winners.append(player)
                        if not found_contradiction:
                            break  # No more FU losers at minimum, exit loop

                    # Create payments dataframe
                    round_payment_data = {}
                    for player in st.session_state.players:
                        if player in set_winners:
                            round_payment_data[player] = ((st.session_state.bet_amount[-1] * len(set_losers_fu) * 2) + (st.session_state.bet_amount[-1] * len(set_losers_normal))) / len(set_winners)  # Winner gets bet amount from each loser
                        elif player in set_losers_normal:
                            round_payment_data[player] = -st.session_state.bet_amount[-1]  # Loser pays bet amount
                        elif player in set_losers_fu:
                            round_payment_data[player] = -st.session_state.bet_amount[-1] * 2  # FU doubles the bet amount            
                        else:
                            round_payment_data[player] = 0
                    round_payment_data_df = pd.DataFrame([round_payment_data])
                    # Append the payment data to the payments list
                    st.session_state.payments.append(round_payment_data_df)

                st.rerun()  # Rerun to update the display

    # ---------------------
    # 6. Payments Summary
    # ---------------------
    st.sidebar.header(get_text(st.session_state.language, "payments"))
    # for i, payment in enumerate(st.session_state.payments):
    #     st.sidebar.write(f"Set {i+1}: {payment}")

    if st.sidebar.button(get_text(st.session_state.language, "settle_payments")):
        all_players = st.session_state.players
        totals = {p: 0 for p in all_players}
        for payment_df in st.session_state.payments:
            payment_dict = payment_df.iloc[0].to_dict()
            for player, amt in payment_dict.items():
                totals[player] += amt
        st.sidebar.write("### " + get_text(st.session_state.language, "net_totals"))
        for player, total in totals.items():
            st.sidebar.write(f"{player}: ${total:.2f}")
