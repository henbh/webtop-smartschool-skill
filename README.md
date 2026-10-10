# Webtop for parents | Webtop להורים

Turn your child's [Smartschool Webtop](https://webtop.smartschool.co.il/) records into Hebrew homework lists, weekly reports, and messages ready to copy into WhatsApp or Telegram.

This is a skill for an AI assistant: install it once, then ask for the report you need. It reads the school records available to your account. It is a community project, independent of Smartschool and the Ministry of Education.

## מתחילים כאן — להורים

1. צריך אפליקציית Codex עם גישה ל־Chrome המחובר שלכם ותוסף הדפדפן המתאים מופעל. התקנת הסקיל לבדה אינה מחברת את הדפדפן.
2. התקינו את הסקיל לפי ההוראות בהמשך. למסלול הרגיל דרך Chrome אין צורך ב־Python או בשרת MCP.
3. פתחו את [Webtop](https://webtop.smartschool.co.il/) ב־Chrome, התחברו כרגיל ובחרו את הילד או הילדה ואת שנת הלימודים. אפשר להתחבר דרך משרד החינוך במסלול זה; אין צורך למסור לסקיל את הסיסמה.
4. פתחו שיחה חדשה ובקשו: `$webtop הצג את שיעורי הבית של השבוע עבור [שם הילד/ה] בטבלה בעברית` — החליפו את הסוגריים בשם הילד או הילדה.
5. בדקו בדוח הראשון שהשם, התאריכים והמטלות תואמים לאתר. אם יש כמה ילדים, ציינו עבור מי הדוח. אם חסרה גישה לחלק מהמידע, הדוח צריך לציין זאת.

**התחברות משרד החינוך:** השתמשו במסלול Chrome. שרת ה־MCP הניסיוני המצורף אינו תומך בכניסה דרך משרד החינוך ואינו משתמש בחיבור הקיים בדפדפן.

## What you need

- An AI assistant that supports skills and can control your connected Chrome browser. The workflow has been used with Codex; other assistants require their own browser setup.
- Chrome with your assistant's browser extension enabled and connected. Follow the browser setup offered by your installed assistant; this repository does not install an extension.
- Access to your child's Webtop records and an active sign-in in that Chrome profile.

**Start with Chrome, including for Ministry of Education SSO.** No API credentials, Python installation, or MCP setup are needed for this route. Available sections depend on your school and account permissions.

## Install in Codex

You can ask Codex:

> Install the skill from https://github.com/henbh/webtop-smartschool-skill with the skill folder named webtop.

For a manual installation:

1. On [this repository](https://github.com/henbh/webtop-smartschool-skill), choose **Code → Download ZIP** and extract it.
2. Create `~/.agents/skills/webtop/`, the personal skill location in the [current official Codex guide](https://developers.openai.com/codex/skills/). `~` means your home folder. On macOS, use Finder → Go → Go to Folder to open a hidden folder.
3. Copy `SKILL.md`, the entire `references/` folder, and `LICENSE` into that folder. Copy the contents directly, without an extra nested repository folder.
4. Start a new Codex chat and type `$webtop`. If it is missing, restart the app and verify the folder layout below.

```text
~/.agents/skills/webtop/
├── SKILL.md
├── LICENSE
└── references/
    └── student-modules.md
```

Existing installations in `~/.codex/skills/webtop/` may already work with your installed version. Update the working copy rather than keeping two skills named `webtop`; follow your app's skill settings and the official guide if it is not discovered. To update manually, replace the skill files from a fresh download. Your local report history is stored separately.

## Your first report

Open Webtop in connected Chrome, select your child and school year, then copy a prompt below. Replace `[שם הילד/ה]` with your child's name.

| What you want | Prompt to copy |
| --- | --- |
| This week's homework | `$webtop הצג את כל שיעורי הבית של השבוע עבור [שם הילד/ה] בטבלה בעברית` |
| Last week's homework | `$webtop הצג את כל שיעורי הבית של השבוע שעבר עבור [שם הילד/ה]` |
| Exact dates | `$webtop הצג שיעורי בית עבור [שם הילד/ה] מ־04/10/2026 עד 10/10/2026` |
| WhatsApp text | `$webtop הכן את שיעורי הבית של השבוע עבור [שם הילד/ה] כהודעת WhatsApp, כולל כל ההנחיות` |
| Tomorrow's timetable | `$webtop הצג את מערכת השעות למחר עבור [שם הילד/ה], כולל שינויים אם קיימים` |
| Grades | `$webtop הצג את הציונים בתקופת הלימודים הנוכחית עבור [שם הילד/ה]` |
| Weekly student report | `$webtop הכן דוח לשבוע שעבר עבור [שם הילד/ה]: שיעורי בית, ציונים, מילים טובות, הערות התנהגות לפי מקצוע, סיכום חיסורים ואיחורים מתחילת השנה ומערכת שעות נוכחית` |
| Teacher messages | `$webtop סכם את הודעות המורים מהשבוע עבור [שם הילד/ה], כולל מועדי הגשה` |
| New updates | `$webtop בדוק עבור [שם הילד/ה] מה חדש או השתנה מאז הבדיקה הקודמת בכל הסעיפים הזמינים` |

English also works: `Use $webtop to list last week's homework for [child's name] in a Hebrew table.`

With several children, request one child at a time or explicitly ask for a separate report for each named child. The assistant should verify the selected child before reading and keep their histories separate. You may need to switch children in the portal if the assistant cannot do so.

## Example results

**All names, dates, assignments, and counts below are fictional examples.** Actual reports depend on records available in your school. Homework dates are lesson dates, not necessarily the date a teacher posted an assignment.

### Homework table

תלמיד/ה: נועה (דוגמה) | 04–10/10/2026 | לפי תאריך השיעור

| תאריך השיעור | מקצוע | מורה | שיעורי בית | מועד הגשה | קבצים / הערות |
| --- | --- | --- | --- | --- | --- |
| 07/10/2026 | חשבון | דנה | להשלים בספר עמודים 42–43, שאלות 1–5. את החישובים לכתוב במחברת. מי שלא סיים בכיתה ישלים גם שאלה 6. | לא צוין | — |
| 08/10/2026 | עברית | יעל | לקרוא את הטקסט ולענות על שאלות 1–3 במשפטים מלאים. | 11/10/2026 | קובץ: reading.pdf |

Long assignments should retain every instruction, page number, question, and condition, including when formatted for WhatsApp. A lesson topic on its own is not homework. Missing information or unreadable attachments should be identified explicitly.

### Weekly report excerpt

```text
📚 דוח שבועי לדוגמה — נועה | 04–10/10/2026

מילים טובות: 3 רשומות — חשבון (2), עברית (1).
הערות התנהגות: 2 רשומות — עברית (1), מדעים (1).

מתחילת שנת הלימודים ועד 10/10/2026:
• חיסורים: 2 | איחורים: 4
• מילים טובות: 8 | הערות התנהגות: 3
המספרים הם ספירת רשומות זמינות באתר, לא מספר ימי היעדרות.

מערכת שעות נוכחית — יום א׳:
שיעור 1: חשבון; שיעור 2: עברית.
שינויים במערכת: לא ניתן לבדוק — אין הרשאה.
```

A full report also includes the requested homework, grades, event details, and messages. Annual statistics require records covering the relevant school year through the report date. If coverage is incomplete, the report must state that. The current timetable cannot establish what was taught in a past week.

## Daily updates at 17:00

Scheduling is optional and is **not activated by installing this skill**. First check that a manual report works, then create a recurring task in an assistant that supports scheduling and has access to your connected Chrome. Choose your children, time, and timezone; for example, **daily at 17:00, Asia/Jerusalem**.

Suggested task prompt:

> Use $webtop for [child's name]. Check homework, grades, attendance, lesson events, timetable changes, and teacher messages for new or changed records since the previous successful check. Prepare a Hebrew WhatsApp-ready update, list any sections that could not be checked, and save observations separately for this child. Preserve the complete homework instructions.

For homework only, replace the list of sections with “homework.” On the first successful check, existing records establish a baseline; they are not all labeled newly posted. Teachers may add homework to earlier lesson dates, so later checks revisit the saved range.

**Delivery choices:**

- **Copy yourself (default):** the assistant prepares WhatsApp or Telegram text in the chat.
- **Automatic sending:** you must separately configure a supported WhatsApp or Telegram integration and explicitly authorize the recipient and channel. This repository includes no messaging integration. Add `Send the update via [WhatsApp or Telegram] to [exact recipient configured for this task]` only after that setup works. If delivery is unavailable, the assistant should return the prepared text and say it was not sent.

Example prepared message:

```text
📚 *עדכון Webtop יומי — נועה | 08/10/2026*

*שיעורי בית חדשים או שהשתנו*
• עברית, 8/10: לקרוא את הטקסט ולענות על שאלות 1–3 במשפטים מלאים.
  להגשה: 11/10. קובץ מצורף: reading.pdf.

*מילים טובות*
• חשבון: נוספה מילה טובה על השתתפות בשיעור.

*הודעות מורים*
• להביא מחברת ביום ראשון.

שינויים במערכת: לא ניתן לבדוק — אין הרשאה.
ההודעה מוכנה להעתקה; לא נשלחה אוטומטית.
```

For this local Chrome workflow, the computer must be awake, the assistant available to run the task, Chrome connected, and Webtop signed in. A session may expire and require you to sign in again. Confirm the task exists in your scheduler and review the first scheduled result; a prompt alone does not create a schedule.

## Dates, history, and privacy

- “Last week” means the previous completed Sunday–Saturday week in Israel time. “Last seven days” means today plus the previous six days. Reports state exact dates; you can always supply your own range.
- Full homework lists include previously reported assignments. “New updates” compares against saved observations; it does not track whether your child completed homework.
- Reports and observations are saved locally in `~/smartschool-homework` unless you choose another folder. A fresh installation starts with no history; separate records by child, school year, and report section.
- When signed out, the assistant may use saved history only if it covers your request. It must label it as cached and show the last check time.
- Reports contain children's personal information. Keep history outside the public repository. Information read by the assistant is processed under that assistant provider's settings and policies; local history does not mean all processing stays on your device.
- Sign in directly on the official portal. Do not put passwords or session tokens in chat, the skill files, saved reports, or GitHub issues.

## Troubleshooting

| Problem | What to do |
| --- | --- |
| `$webtop` is missing | Check the installation folder and `SKILL.md` location, then restart the assistant. |
| Chrome cannot be reached | Enable your assistant's Chrome extension and connect the correct browser profile. Skill installation alone does not provide browser access. |
| Webtop asks you to sign in | Sign in in Chrome, including Ministry of Education SSO if that is your usual method, then retry. |
| The wrong child is selected | Select the intended child in Webtop and include their name in the request. |
| Homework or a date is missing | Ask for the exact date range, including a recheck of every homework cell and attachment. Compare with the portal; a partial read is not a complete report. |
| A section says “no permission” | That section is unavailable for your account. Ask for the accessible sections; permissions vary by school. |
| A scheduled message did not arrive | Check the task actually ran, the computer was awake, Chrome/login were available, and sending was configured for the correct recipient. |

For help, [open an issue](https://github.com/henbh/webtop-smartschool-skill/issues) describing the step that failed and your assistant/browser setup. Remove child names, school details, credentials, and student records from examples or screenshots.

## Claude Code

Install `SKILL.md`, `references/`, and `LICENSE` in `~/.claude/skills/webtop/` and invoke `/webtop`; see the [Claude Code skills guide](https://code.claude.com/docs/en/skills). You must separately configure a compatible browser integration. This workflow has not been validated end to end in Claude Code.

## Experimental MCP — advanced setup

An MCP server lets an assistant call Webtop API tools directly. The optional [MCP guide](mcp-server/README.md) covers the current `get_dashboard` and `get_homework` tools. It does not provide the full browser report workflow.

**Ministry of Education SSO is not supported by this MCP.** It also cannot reuse your signed-in Chrome session. Its unofficial API client supports direct Webtop username/password login only. MCP startup and tool discovery have been tested; successful live homework retrieval has not yet been verified. Parents using SSO should use the Chrome workflow above.

## License and project files

Copyright 2026 Hen Ben-Hemo. This project's skill instructions, documentation, and MCP code are licensed under the [Apache License 2.0](LICENSE). Dependencies retain their own licenses; see the [MCP guide](mcp-server/README.md#license-and-dependencies). This license does not grant rights to Smartschool's service, trademarks, or student records.

- [SKILL.md](SKILL.md): instructions followed by the assistant.
- [Student modules](references/student-modules.md): timetable, grades, events, and messages.
- [MCP guide](mcp-server/README.md): optional developer setup and limitations.
