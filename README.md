# 跑得快 (Paodekuai) Game Tracker

> Pork rib soup, ngoh hiang, mandarin oranges, angpaos. 
> It is that time of the year again.  
> Shu shu rushes home from the countryside, jie jie flies in from the big city.  
> Full attendance, digging into grandma’s delicious cooking.  
> Chun wan in the background, poker cards on the table.  
> Paodekuai, the only time where the kids can gamble.  

This Streamlit application was born from a chaotic but joyful Chinese New Year, when we realized keeping track of **Paodekuai** scores and payments often led to inefficiencies and disagreements. [Try it online here](https://paodekuai.streamlit.app/).  

---

## About Paodekuai

**Paodekuai** (跑得快, literally "Run Fast") is a popular Chinese shedding-type card game, commonly played in families and among friends. The goal is simple: be the first to play all your cards. While the rules vary regionally, this tracker implements **my family's unique version**.

### Brief Rules (Family Version)

- Players: 2–10  
- Objective: Be the first to empty your hand  
- Game Play: Cards are played in singles, pairs, or sequences; each play must beat the previous [Standard sequences here](https://baike.baidu.com/item/%E8%B7%91%E5%BE%97%E5%BF%AB/12998100)
- Special Rules:  
  - "俘了" - a special status that occurs when a round ends with at least one player who has not emptied a single card from their hand. The set will automatically end, and the player will lose double the initial bet to the player with the lowest number of cards in the set.
- Scoring: Wins and losses are calculated per round, with automatic tracking for ongoing totals  

---

## Features

- **Bilingual Support**: Switch between English and Chinese interfaces  
- **Game Tracking**: Manage multiple sets, rounds, and player statistics  
- **Payment Management**: Automatically calculate and track payments between players  
- **Data Export**: Save game results as CSV  
- **Responsive UI**: Clean, modern interface with wide layout support  

---

## Quick Start

### Installation

```bash
pip install -r requirements.txt
streamlit run main.py
