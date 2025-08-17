# Translations for Paodekuai Game Tracker
# English and Chinese language support

TRANSLATIONS = {
    "en": {
        "page_title": "Paodekuai Game Tracker",
        "game_setup": "Game Setup",
        "num_players": "Number of players",
        "player_name": "Player {num} Name",
        "start_new_game": "Start New Game",
        "warning_enter_names": "Please enter a name for every player.",
        "warning_unique_names": "Player names must be unique.",
        "main_title": "Paodekuai Game Tracker",
        "main_description": "Track your game progress, payments, and player stats.",
        "export_to_csv": "Export to CSV",
        "download_csv": "Download CSV",
        "please_start_game": "Please start a new game from the left panel.",
        "set": "Set {num}",
        "delete": "🗑️ Delete",
        "bet_amount": "Bet Amount: ${amount}",
        "elimination_threshold": "Elimination Threshold: {threshold} cards",
        "starting_cards": "Starting Cards: {cards} per player",
        "payments_for_set": "Payments for Set {num}:",
        "add_new_set": "Add New Set",
        "bet_amount_per_set": "Bet amount per set ($)",
        "elimination_threshold_cards": "Elimination threshold (cards)",
        "starting_cards_per_player": "Starting cards per player",
        "add": "Add",
        "set_round": "Set {set_num} Round {round_num}",
        "cards_remaining": "Cards remaining for {player}",
        "add_round": "Add Round",
        "warning_one_winner": "Only one player can have 0 cards remaining. Please check your input.",
        "warning_need_winner": "At least one player must have 0 cards remaining to end the round.",
        "warning_exceeded_cards": "The following players have more cards than the starting amount: {players}. Please check your input.",
        "payments": "Payments",
        "settle_payments": "Settle Payments",
        "net_totals": "Net Totals",
        "language_selector": "Language / 语言",
        "fu_toast": "俘了",
        "rounds": "Rounds",
        "payment": "Payment ($)",
        "total": "Total"
    },
    "zh": {
        "page_title": "跑得快游戏追踪器",
        "game_setup": "游戏设置",
        "num_players": "玩家数量",
        "player_name": "玩家 {num} 姓名",
        "start_new_game": "开始新游戏",
        "warning_enter_names": "请为每个玩家输入姓名。",
        "warning_unique_names": "玩家姓名必须唯一。",
        "main_title": "跑得快游戏追踪器",
        "main_description": "追踪您的游戏进度、支付和玩家统计。",
        "export_to_csv": "导出到CSV",
        "download_csv": "下载CSV",
        "please_start_game": "请从左侧面板开始新游戏。",
        "set": "第 {num} 局",
        "delete": "🗑️ 删除",
        "bet_amount": "下注金额: ${amount}",
        "elimination_threshold": "淘汰阈值: {threshold} 张牌",
        "starting_cards": "起始牌数: 每人 {cards} 张",
        "payments_for_set": "第 {num} 局支付:",
        "add_new_set": "添加新局",
        "bet_amount_per_set": "每局下注金额 ($)",
        "elimination_threshold_cards": "淘汰阈值 (张牌)",
        "starting_cards_per_player": "每人起始牌数",
        "add": "添加",
        "set_round": "第 {set_num} 局 第 {round_num} 轮",
        "cards_remaining": "{player} 剩余牌数",
        "add_round": "添加轮次",
        "warning_one_winner": "只有一名玩家可以剩余0张牌。请检查您的输入。",
        "warning_need_winner": "至少有一名玩家必须剩余0张牌才能结束轮次。",
        "warning_exceeded_cards": "以下玩家的牌数超过了起始数量: {players}。请检查您的输入。",
        "payments": "支付",
        "settle_payments": "结算支付",
        "net_totals": "净总额",
        "language_selector": "Language / 语言",
        "fu_toast": "俘了",
        "rounds": "轮次",
        "payment": "支付 ($)",
        "total": "总计"
    }
}

def get_text(lang, key, **kwargs):
    """Get translated text for the given language and key, with optional formatting"""
    if lang not in TRANSLATIONS:
        lang = "en"  # Default to English if language not found
    
    text = TRANSLATIONS[lang].get(key, key)
    
    # Format the text with any provided kwargs
    if kwargs:
        try:
            text = text.format(**kwargs)
        except KeyError:
            pass  # If formatting fails, return the original text
    
    return text
