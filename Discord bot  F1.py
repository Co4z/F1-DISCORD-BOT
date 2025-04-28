import discord
from discord.ext import commands
from datetime import datetime
import pytz

# --- การจัดการ Token (แนะนำ) ---
 K = ""

# --- ตั้งค่า Bot ---
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# --- กำหนด Timezone เป้าหมาย ---
TARGET_TIMEZONE = 'Asia/Bangkok'  # โซนเวลาไทย
target_tz = pytz.timezone(TARGET_TIMEZONE)

# --- ตารางข้อมูลการแข่งขัน F1 ---
schedule = [
    # Saudi Arabia
    {"location": "Saudi Arabia", "race_date": "2025-04-18 13:30:00", "event": "Practice 1", "local_time": "13:30", "time_in_thai": "20:30"},
    {"location": "Saudi Arabia", "race_date": "2025-04-18 17:00:00", "event": "Practice 2", "local_time": "17:00", "time_in_thai": "00:00"},
    {"location": "Saudi Arabia", "race_date": "2025-04-19 13:30:00", "event": "Practice 3", "local_time": "13:30", "time_in_thai": "20:30"},
    {"location": "Saudi Arabia", "race_date": "2025-04-19 17:00:00", "event": "Qualifying", "local_time": "17:00", "time_in_thai": "00:00"},
    {"location": "Saudi Arabia", "race_date": "2025-04-20 17:00:00", "event": "Race", "local_time": "17:00", "time_in_thai": "00:00"},

    # Miami
    {"location": "Miami", "race_date": "2025-05-02 16:30:00", "event": "Practice 1", "local_time": "16:30", "time_in_thai": "23:30"},
    {"location": "Miami", "race_date": "2025-05-02 20:30:00", "event": "Sprint Qualifying", "local_time": "20:30", "time_in_thai": "03:30"},
    {"location": "Miami", "race_date": "2025-05-03 16:00:00", "event": "Sprint", "local_time": "16:00", "time_in_thai": "23:00"},
    {"location": "Miami", "race_date": "2025-05-03 20:00:00", "event": "Qualifying", "local_time": "20:00", "time_in_thai": "03:00"},
    {"location": "Miami", "race_date": "2025-05-04 20:00:00", "event": "Race", "local_time": "20:00", "time_in_thai": "03:00"},

    # Emiliaromagna
    {"location": "Emiliaromagna", "race_date": "2025-05-16 11:30:00", "event": "Practice 1", "local_time": "11:30", "time_in_thai": "18:30"},
    {"location": "Emiliaromagna", "race_date": "2025-05-16 15:00:00", "event": "Practice 2", "local_time": "15:00", "time_in_thai": "22:00"},
    {"location": "Emiliaromagna", "race_date": "2025-05-17 10:30:00", "event": "Practice 3", "local_time": "10:30", "time_in_thai": "17:30"},
    {"location": "Emiliaromagna", "race_date": "2025-05-17 14:00:00", "event": "Qualifying", "local_time": "14:00", "time_in_thai": "21:00"},
    {"location": "Emiliaromagna", "race_date": "2025-05-18 13:00:00", "event": "Race", "local_time": "13:00", "time_in_thai": "20:00"},

    # Monaco
    {"location": "Monaco", "race_date": "2025-05-23 11:30:00", "event": "Practice 1", "local_time": "11:30", "time_in_thai": "18:30"},
    {"location": "Monaco", "race_date": "2025-05-23 15:00:00", "event": "Practice 2", "local_time": "15:00", "time_in_thai": "22:00"},
    {"location": "Monaco", "race_date": "2025-05-24 10:30:00", "event": "Practice 3", "local_time": "10:30", "time_in_thai": "17:30"},
    {"location": "Monaco", "race_date": "2025-05-24 14:00:00", "event": "Qualifying", "local_time": "14:00", "time_in_thai": "21:00"},
    {"location": "Monaco", "race_date": "2025-05-25 13:00:00", "event": "Race", "local_time": "13:00", "time_in_thai": "20:00"},

    # Spain
    {"location": "Spain", "race_date": "2025-05-30 11:30:00", "event": "Practice 1", "local_time": "11:30", "time_in_thai": "18:30"},
    {"location": "Spain", "race_date": "2025-05-30 15:00:00", "event": "Practice 2", "local_time": "15:00", "time_in_thai": "22:00"},
    {"location": "Spain", "race_date": "2025-05-31 10:30:00", "event": "Practice 3", "local_time": "10:30", "time_in_thai": "17:30"},
    {"location": "Spain", "race_date": "2025-05-31 14:00:00", "event": "Qualifying", "local_time": "14:00", "time_in_thai": "21:00"},
    {"location": "Spain", "race_date": "2025-06-01 13:00:00", "event": "Race", "local_time": "13:00", "time_in_thai": "20:00"},

    # Canada
    {"location": "Canada", "race_date": "2025-06-13 17:30:00", "event": "Practice 1", "local_time": "17:30", "time_in_thai": "00:30"},
    {"location": "Canada", "race_date": "2025-06-13 21:00:00", "event": "Practice 2", "local_time": "21:00", "time_in_thai": "04:00"},
    {"location": "Canada", "race_date": "2025-06-14 16:30:00", "event": "Practice 3", "local_time": "16:30", "time_in_thai": "23:30"},
    {"location": "Canada", "race_date": "2025-06-14 20:00:00", "event": "Qualifying", "local_time": "20:00", "time_in_thai": "03:00"},
    {"location": "Canada", "race_date": "2025-06-15 18:00:00", "event": "Race", "local_time": "18:00", "time_in_thai": "01:00"},

    # Austria
    {"location": "Austria", "race_date": "2025-06-27 11:30:00", "event": "Practice 1", "local_time": "11:30", "time_in_thai": "18:30"},
    {"location": "Austria", "race_date": "2025-06-27 15:00:00", "event": "Practice 2", "local_time": "15:00", "time_in_thai": "22:00"},
    {"location": "Austria", "race_date": "2025-06-28 10:30:00", "event": "Practice 3", "local_time": "10:30", "time_in_thai": "17:30"},
    {"location": "Austria", "race_date": "2025-06-28 14:00:00", "event": "Qualifying", "local_time": "14:00", "time_in_thai": "21:00"},
    {"location": "Austria", "race_date": "2025-06-29 13:00:00", "event": "Race", "local_time": "13:00", "time_in_thai": "20:00"},

    # Great Britain
    {"location": "Great Britain", "race_date": "2025-07-04 11:30:00", "event": "Practice 1", "local_time": "11:30", "time_in_thai": "18:30"},
    {"location": "Great Britain", "race_date": "2025-07-04 15:00:00", "event": "Practice 2", "local_time": "15:00", "time_in_thai": "22:00"},
    {"location": "Great Britain", "race_date": "2025-07-05 10:30:00", "event": "Practice 3", "local_time": "10:30", "time_in_thai": "17:30"},
    {"location": "Great Britain", "race_date": "2025-07-05 14:00:00", "event": "Qualifying", "local_time": "14:00", "time_in_thai": "21:00"},
    {"location": "Great Britain", "race_date": "2025-07-06 14:00:00", "event": "Race", "local_time": "14:00", "time_in_thai": "21:00"},

    # Belgium
    {"location": "Belgium", "race_date": "2025-07-25 10:30:00", "event": "Practice 1", "local_time": "10:30", "time_in_thai": "17:30"},
    {"location": "Belgium", "race_date": "2025-07-25 14:30:00", "event": "Sprint Qualifying", "local_time": "14:30", "time_in_thai": "21:30"},
    {"location": "Belgium", "race_date": "2025-07-26 10:00:00", "event": "Sprint", "local_time": "10:00", "time_in_thai": "17:00"},
    {"location": "Belgium", "race_date": "2025-07-26 14:00:00", "event": "Qualifying", "local_time": "14:00", "time_in_thai": "21:00"},
    {"location": "Belgium", "race_date": "2025-07-27 13:00:00", "event": "Race", "local_time": "13:00", "time_in_thai": "20:00"},

    # Hungary
    {"location": "Hungary", "race_date": "2025-08-01 11:30:00", "event": "Practice 1", "local_time": "11:30", "time_in_thai": "18:30"},
    {"location": "Hungary", "race_date": "2025-08-01 15:00:00", "event": "Practice 2", "local_time": "15:00", "time_in_thai": "22:00"},
    {"location": "Hungary", "race_date": "2025-08-02 10:30:00", "event": "Practice 3", "local_time": "10:30", "time_in_thai": "17:30"},
    {"location": "Hungary", "race_date": "2025-08-02 14:00:00", "event": "Qualifying", "local_time": "14:00", "time_in_thai": "21:00"},
    {"location": "Hungary", "race_date": "2025-08-03 13:00:00", "event": "Race", "local_time": "13:00", "time_in_thai": "20:00"},

    # Netherlands
    {"location": "Netherlands", "race_date": "2025-08-29 10:30:00", "event": "Practice 1", "local_time": "10:30", "time_in_thai": "17:30"},
    {"location": "Netherlands", "race_date": "2025-08-29 14:00:00", "event": "Practice 2", "local_time": "14:00", "time_in_thai": "21:00"},
    {"location": "Netherlands", "race_date": "2025-08-30 09:30:00", "event": "Practice 3", "local_time": "09:30", "time_in_thai": "16:30"},
    {"location": "Netherlands", "race_date": "2025-08-31 13:00:00", "event": "Race", "local_time": "13:00", "time_in_thai": "20:00"},

    # Italy
    {"location": "Italy", "race_date": "2025-09-07 13:00:00", "event": "Race", "local_time": "13:00", "time_in_thai": "20:00"},
    {"location": "Italy", "race_date": "2025-09-06 14:00:00", "event": "Qualifying", "local_time": "14:00", "time_in_thai": "21:00"},
    {"location": "Italy", "race_date": "2025-09-06 10:30:00", "event": "Practice 3", "local_time": "10:30", "time_in_thai": "17:30"},
    {"location": "Italy", "race_date": "2025-09-05 15:00:00", "event": "Practice 2", "local_time": "15:00", "time_in_thai": "22:00"},
    {"location": "Italy", "race_date": "2025-09-05 11:30:00", "event": "Practice 1", "local_time": "11:30", "time_in_thai": "18:30"},

    # Azerbaijan
    {"location": "Azerbaijan", "race_date": "2025-09-21 11:00:00", "event": "Race", "local_time": "11:00", "time_in_thai": "18:00"},
    {"location": "Azerbaijan", "race_date": "2025-09-20 12:00:00", "event": "Qualifying", "local_time": "12:00", "time_in_thai": "19:00"},
    {"location": "Azerbaijan", "race_date": "2025-09-20 08:30:00", "event": "Practice 3", "local_time": "08:30", "time_in_thai": "15:30"},
    {"location": "Azerbaijan", "race_date": "2025-09-19 12:00:00", "event": "Practice 2", "local_time": "12:00", "time_in_thai": "19:00"},
    {"location": "Azerbaijan", "race_date": "2025-09-19 08:30:00", "event": "Practice 1", "local_time": "08:30", "time_in_thai": "15:30"},

    # Singapore
    {"location": "Singapore", "race_date": "2025-10-05 12:00:00", "event": "Race", "local_time": "12:00", "time_in_thai": "19:00"},
    {"location": "Singapore", "race_date": "2025-10-04 13:00:00", "event": "Qualifying", "local_time": "13:00", "time_in_thai": "20:00"},
    {"location": "Singapore", "race_date": "2025-10-04 09:30:00", "event": "Practice 3", "local_time": "09:30", "time_in_thai": "16:30"},
    {"location": "Singapore", "race_date": "2025-10-03 13:00:00", "event": "Practice 2", "local_time": "13:00", "time_in_thai": "20:00"},
    {"location": "Singapore", "race_date": "2025-10-03 09:30:00", "event": "Practice 1", "local_time": "09:30", "time_in_thai": "16:30"},

    # United States
    {"location": "United States", "race_date": "2025-10-19 19:00:00", "event": "Race", "local_time": "19:00", "time_in_thai": "02:00"},
    {"location": "United States", "race_date": "2025-10-18 21:00:00", "event": "Qualifying", "local_time": "21:00", "time_in_thai": "04:00"},
    {"location": "United States", "race_date": "2025-10-18 17:00:00", "event": "Sprint", "local_time": "17:00", "time_in_thai": "00:00"},
    {"location": "United States", "race_date": "2025-10-17 21:30:00", "event": "Sprint Qualifying", "local_time": "21:30", "time_in_thai": "04:30"},
    {"location": "United States", "race_date": "2025-10-17 17:30:00", "event": "Practice 1", "local_time": "17:30", "time_in_thai": "00:30"},

    # Mexico
    {"location": "Mexico", "race_date": "2025-10-26 20:00:00", "event": "Race", "local_time": "20:00", "time_in_thai": "03:00"},
    {"location": "Mexico", "race_date": "2025-10-25 21:00:00", "event": "Qualifying", "local_time": "21:00", "time_in_thai": "04:00"},
    {"location": "Mexico", "race_date": "2025-10-25 17:30:00", "event": "Practice 3", "local_time": "17:30", "time_in_thai": "00:30"},
    {"location": "Mexico", "race_date": "2025-10-24 22:00:00", "event": "Practice 2", "local_time": "22:00", "time_in_thai": "05:00"},
    {"location": "Mexico", "race_date": "2025-10-24 18:30:00", "event": "Practice 1", "local_time": "18:30", "time_in_thai": "01:30"},

    # Brazil
    {"location": "Brazil", "race_date": "2025-11-09 17:00:00", "event": "Race", "local_time": "17:00", "time_in_thai": "00:00"},
    {"location": "Brazil", "race_date": "2025-11-08 18:00:00", "event": "Qualifying", "local_time": "18:00", "time_in_thai": "01:00"},
    {"location": "Brazil", "race_date": "2025-11-08 14:00:00", "event": "Sprint", "local_time": "14:00", "time_in_thai": "21:00"},
    {"location": "Brazil", "race_date": "2025-11-07 18:30:00", "event": "Sprint Qualifying", "local_time": "18:30", "time_in_thai": "01:30"},
    {"location": "Brazil", "race_date": "2025-11-07 14:30:00", "event": "Practice 1", "local_time": "14:30", "time_in_thai": "21:30"},

    # Las Vegas
    {"location": "Las Vegas", "race_date": "2025-11-23 04:00:00", "event": "Race", "local_time": "04:00", "time_in_thai": "11:00"},
    {"location": "Las Vegas", "race_date": "2025-11-22 04:00:00", "event": "Qualifying", "local_time": "04:00", "time_in_thai": "11:00"},
    {"location": "Las Vegas", "race_date": "2025-11-22 00:30:00", "event": "Practice 3", "local_time": "00:30", "time_in_thai": "07:30"},
    {"location": "Las Vegas", "race_date": "2025-11-21 04:00:00", "event": "Practice 2", "local_time": "04:00", "time_in_thai": "11:00"},
    {"location": "Las Vegas", "race_date": "2025-11-21 00:30:00", "event": "Practice 1", "local_time": "00:30", "time_in_thai": "07:30"},

    # Qatar
    {"location": "Qatar", "race_date": "2025-11-30 16:00:00", "event": "Race", "local_time": "16:00", "time_in_thai": "23:00"},
    {"location": "Qatar", "race_date": "2025-11-29 18:00:00", "event": "Qualifying", "local_time": "18:00", "time_in_thai": "01:00"},
    {"location": "Qatar", "race_date": "2025-11-29 14:00:00", "event": "Sprint", "local_time": "14:00", "time_in_thai": "21:00"},
    {"location": "Qatar", "race_date": "2025-11-28 17:30:00", "event": "Sprint Qualifying", "local_time": "17:30", "time_in_thai": "00:30"},
    {"location": "Qatar", "race_date": "2025-11-28 13:30:00", "event": "Practice 1", "local_time": "13:30", "time_in_thai": "20:30"},

    # United-arab-emirates
    {"location": "United-arab-emirates", "race_date": "2025-12-07 13:00:00", "event": "Race", "local_time": "13:00", "time_in_thai": "20:00"},
    {"location": "United-arab-emirates", "race_date": "2025-12-06 14:00:00", "event": "Qualifying", "local_time": "14:00", "time_in_thai": "21:00"},
    {"location": "United-arab-emirates", "race_date": "2025-12-06 10:30:00", "event": "Practice 3", "local_time": "10:30", "time_in_thai": "17:30"},
    {"location": "United-arab-emirates", "race_date": "2025-12-05 13:00:00", "event": "Practice 2", "local_time": "13:00", "time_in_thai": "20:00"},

]

# --- คำสั่ง !calendar ---
@bot.command(name='calendar', help='แสดงปฏิทินการแข่งขัน F1')
async def show_calendar(ctx):
    """
    แสดงปฏิทินการแข่งขัน F1 โดยแสดงแค่วันเวลา และสถานที่การแข่งขัน ในรูปแบบ Embeds ที่สวยงาม
    """
    now = datetime.now(target_tz)  # ใช้เวลาในโซนเวลาของประเทศไทย
    future_races = []

    # กรองเฉพาะสนามแข่งที่ยังไม่เกิดขึ้น
    for event in schedule:
        event_time = datetime.strptime(event["race_date"], "%Y-%m-%d %H:%M:%S")
        event_time = target_tz.localize(event_time)  # กำหนดเวลาให้ตรงกับโซนเวลาไทย
        if event_time > now and event["event"] == "Race":  # แสดงเฉพาะวันแข่งจริง
            future_races.append(event)

    if future_races:
        # เรียงลำดับสนามแข่งตามเวลาที่ใกล้เคียงกับเวลาปัจจุบันมากที่สุด
        future_races.sort(key=lambda x: datetime.strptime(x["race_date"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=target_tz), reverse=False)

        embed = discord.Embed(
            title="️ ปฏิทินการแข่งขัน F1 ️",
            color=discord.Color.red()  # กำหนดสีของ Embed
        )

        for race in future_races:
            race_date = datetime.strptime(race["race_date"], "%Y-%m-%d %H:%M:%S").strftime("%d %b %Y")  # รูปแบบวันที่ 07 Sep 2025
            embed.add_field(
                name=f"**{race['location']}**",
                value=f" {race_date} ⏰ {race['time_in_thai']} (เวลาไทย)",
                inline=False  # แสดงแต่ละสนามในบรรทัดใหม่
            )

        await ctx.send(embed=embed)
    else:
        await ctx.send("ไม่พบสนามแข่งถัดไปในข้อมูลที่มีอยู่")


@bot.event
async def on_ready():
    print(f'บอท {bot.user} พร้อมใช้งานแล้ว!')

# --- คำสั่ง !upnext ---
@bot.command(name='upnext', help='แสดงสนามถัดไปและกิจกรรมทั้งหมด')
async def get_next_f1_race(ctx):
    """
    แสดงสนามแข่ง F1 ถัดไปและกิจกรรมทั้งหมดในรูปแบบ Embeds ที่สวยงาม
    """
    now = datetime.now(target_tz)  # ใช้เวลาในโซนเวลาของประเทศไทย
    future_events = []

    # กรองเฉพาะกิจกรรมที่ยังไม่เกิดขึ้นและจัดเก็บใน future_events
    for event in schedule:
        event_time = datetime.strptime(event["race_date"], "%Y-%m-%d %H:%M:%S")
        event_time = target_tz.localize(event_time)  # กำหนดเวลาให้ตรงกับโซนเวลาไทย
        if event_time > now:
            future_events.append(event)

    if future_events:
        # เรียงลำดับกิจกรรมตามเวลาที่ใกล้เคียงกับเวลาปัจจุบันมากที่สุด
        future_events.sort(key=lambda x: datetime.strptime(x["race_date"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=target_tz), reverse=False)

        # แสดงข้อมูลสนามถัดไปและกิจกรรมทั้งหมด
        next_event = future_events[0]
        events_in_next_race = [e for e in future_events if e["location"] == next_event["location"]]

        embed = discord.Embed(
            title=f"️ สนามถัดไป: {next_event['location']} ️",
            color=discord.Color.blue()  # กำหนดสีของ Embed
        )

        embed.add_field(name="⏳ กิจกรรมทั้งหมด ⏳", value="", inline=False)  # เพิ่มหัวข้อกิจกรรม

        # เรียงลำดับกิจกรรมตามวันที่และเวลา
        events_in_next_race.sort(key=lambda x: datetime.strptime(x["race_date"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=target_tz), reverse=True)

        for e in events_in_next_race:
            event_date = datetime.strptime(e["race_date"], "%Y-%m-%d %H:%M:%S").strftime("%d %b")  # รูปแบบวันที่ 06 Sep
            embed.add_field(
                name=f" {event_date} - {e['event']}",
                value=f"⏰ {e['local_time']} (เวลาไทย: {e['time_in_thai']})",
                inline=False  # แสดงแต่ละกิจกรรมในบรรทัดใหม่
            )

        await ctx.send(embed=embed)
    else:
        await ctx.send("ไม่พบสนามถัดไปในข้อมูลที่มีอยู่")
        
bot.run(K)