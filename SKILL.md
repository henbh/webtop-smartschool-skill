---
name: webtop
description: Read the Smartschool Webtop student portal through connected Chrome. Produce Hebrew homework, timetable, grades, attendance, lesson-event, and teacher-message reports for requested dates and track homework changes between checks.
license: Apache-2.0
---

# Webtop Smartschool student reports

The product is Smartschool and the student portal is Webtop. For explicit invocation use `$webtop` in Codex or `/webtop` in Claude Code; natural-language requests mentioning either “Smartschool” or “Webtop” should also route here.

## Defaults for each family

- Source: https://webtop.smartschool.co.il/Student_Card/11
- Browser: the user's connected Chrome profile signed in to Smartschool.
- Default one-off output: a Hebrew homework table returned in the chat. When the user asks for a weekly student report/full weekly report, include homework, weekly positive feedback and behavior notes, year-to-date attendance/event statistics, and the current timetable, plus other requested modules.
- Optional output: Hebrew WhatsApp- or Telegram-ready text when requested; the daily update workflow uses this format by default.
- History folder: `~/smartschool-homework`.
- Optional schedule example: daily at 17:00, timezone `Asia/Jerusalem`. Use the family's requested time and children. This skill does not itself activate a schedule. Only report a schedule as active after verifying its creation with a supported scheduling tool or interface.

Use an explicit requested date range for a one-off summary. For recurring checks, revisit the saved coverage range to detect late additions. With no history, use the family's requested range or the start of the selected school year through the current date; verify that year in Webtop rather than hardcoding a calendar year. The user can change these defaults.

## Request modes

- Last week's homework, or a homework list without dates: use the previous completed calendar week, Sunday through Saturday, in Asia/Jerusalem. State its exact dates in the answer. For example, on Saturday 26/09/2026 this means 13–19/09/2026. “Last seven days” instead means today and the preceding six dates. Explicit dates always take precedence.
- A homework table lists every assignment found within the requested range, including previously reported assignments. Do not apply the recurring new-items-only filter to this mode.
- A daily homework update checks new or changed homework only.
- A daily all-updates request checks homework, grades, attendance and lesson events, verifiable timetable changes, and teacher messages against their separate saved observations. Return only new or substantively changed records in a Hebrew WhatsApp-ready message unless another format is requested. Clearly list modules that could not be checked. A first check establishes baselines; it must not describe all existing records as newly added.
- If multiple students are available, use the explicitly requested student or the student established in task history. If neither identifies one unambiguously, ask which student before extracting personal records.
- For requests covering several children, verify each child's selected identity and produce separate reports and observations. Never reuse one child's baseline or records for another child.
- If the connected Webtop tab is signed out, state that live access is unavailable and ask the user to sign in. You may answer from saved local history only when it covers the requested student, module, and dates; label it clearly as cached and include its last checked date. Do not present cached data as a live check. If history is insufficient, wait for sign-in rather than guessing.

## Homework table

Use these Hebrew columns: `תאריך השיעור | מקצוע | מורה | שיעורי בית | מועד הגשה | קבצים / הערות`.

Sort by lesson date and then lesson order. Combine duplicate assignments for the same day and subject while preserving distinct instructions. Include all assigned page numbers and questions in the homework cell. Show `לא צוין` for a deadline not stated by the teacher; never derive a due date from the next scheduled lesson. In the notes column identify subject-label mismatches and attachment names. Put classwork-only entries in a short separate note instead of presenting them as homework.

State the student and exact date range above the table, and clarify that dates are lesson dates. Report days or weeks that could not be read; do not fill missing information from older summaries. If no assignments are shown after a complete read, say so without creating empty table rows.

## Additional Smartschool features

Support timetable and changes, grades, attendance and lesson events, and teacher messages. Read [references/student-modules.md](references/student-modules.md) when one of these modules is requested. A full Smartschool report includes homework and all four additional modules; a homework request remains homework-only.

For a full weekly student report, use the same explicit week for homework, grades, events, and messages, and separate Hebrew tables for each. Include positive feedback and behavior-related notes from the lesson-event records: report the exact displayed category and text, count matching records for the week, and group them by subject when the site provides a reliable subject association. The event's `קבוצת לימוד` displays subject and teacher. Do not relabel academic reminders, missing materials, or other categories as behavior notes. Add year-to-date statistics from the start of the selected school year through the report date for explicitly recorded absences and lateness, plus counts of positive feedback and behavior-related event categories when available. Preserve the site's original category labels (for example, `אי הכנת שיעורי בית`, `אי הבאת ספר קריאה`, and `מילה טובה`) rather than collapsing them into an assumed behavior class. The event counter is filtered by school year and study period (observed: `מחצית א` / `מחצית ב`), not by an annual date range; to produce year-to-date totals, combine the applicable periods and exclude records after the report cutoff, or count fully covered detail rows. The counter has per-category totals and a subject breakdown chart with category/status filters and `קיבוץ מקצועות זהים`. `נוכחות` is a recorded category and must not be counted as an absence; count absence/lateness only from explicit corresponding categories. Call all totals counts of recorded entries, not attendance percentages or unique school days. State the school-year/date coverage and any filter, permission, pagination, or counter limitations. A partial period or first-page-only view cannot support a complete annual total.

Include the current regular timetable in a full weekly student report, using the format and limitations in [references/student-modules.md](references/student-modules.md). Label it as the current timetable; show verifiable changes separately. Never present a current timetable as evidence of past lessons or past schedule changes. Clearly distinguish empty results, incomplete coverage, and permission-denied sections. The daily all-updates mode checks each supported module against its own saved observations.

## Read the homework

For Ministry of Education SSO, use the signed-in Chrome workflow. The experimental MCP does not support SSO or reuse Chrome sessions; do not ask for Ministry credentials or retry them against its direct-login endpoint.

If the optional local Webtop MCP server is configured and its tools are available, you may use `get_dashboard` and `get_homework` to retrieve records. Confirm the dashboard identifies the intended student; use only known class codes and class numbers, and query every applicable class. Verify the returned date coverage and preserve the full original homework text. The private API is unofficial and may be incomplete or out of date; if login fails, required class metadata is missing, or coverage is uncertain, continue with connected Chrome.

Otherwise use the available supported browser automation tool and its current documentation. Discover the connected Chrome tab by its URL; do not persist tab IDs or accessibility element indices. Reuse the signed-in Smartschool tab when available. If Chrome or login is unavailable, explain the access blocker and request the relevant connection or sign-in.

On `נושאי שיעור ושיעורי-בית`, verify the selected student and school year against the requested task or existing history. Read all weeks intersecting the requested range using `שבוע קודם`, `שבוע הבא`, or the visible calendar. Capture each day's homework column with its lesson date, subject, teacher, lesson number, text, and attachment names. Finish reading the displayed state after navigation before continuing.

Interpretation rules derived from this site:

- The `נושא שיעור/סיבת ביטול` column is separate from `שיעורי בית`. A lesson topic alone is not an assignment.
- The displayed dates are lesson dates, not posting timestamps. Describe newly observed entries as new since the previous check; do not claim the teacher posted them on the lesson date.
- `טרם הוזנו נתונים` means data not yet entered. Empty or missing homework is not proof that no work was assigned elsewhere.
- Teachers sometimes enter classwork notes in the homework column or teach Hebrew in a slot labeled Art. Preserve that context without silently changing the recorded subject.
- Preserve exact page ranges, questions, workbook names, notebook-versus-workbook directions, conditional completion instructions, and explicit deadlines. Flag incomplete entries rather than guessing; for example, `עמוד 148-` gives no ending page.
- Completeness is more important than brevity: include the full content shown in each homework cell, not only its opening instruction. This includes embedded explanations, examples, bullet lists, copied board notes, and details that clarify what to practice or complete. Do not silently summarize or omit a long block as “details” or “see explanation”; structure it into readable sub-bullets while preserving all of its content. In WhatsApp output, keep the complete assignment even when it makes the message longer.
- Mention attached files. Inspect an attachment with supported tools when the assignment depends on its contents; if it cannot be read, state that limitation.
- Combine repeated assignments across consecutive lessons, retaining any distinct details.

## History and recurring checks

Read `workflow.md` and relevant previous reports or snapshots in the family's history folder if they exist. A new installation has no baseline: create the folder and establish observations after the first successful read. Keep separate child/school-year records, using subfolders or clearly identified files; preserve existing history and compare only matching identities, years, and modules. This is local task memory, not cross-session model memory.

For recurring homework checks, revisit the saved date range to detect late additions to earlier lessons. Compare assignment content, not just the lesson date. Return only new or substantively changed assignments, clearly labeling changes. Do not infer completion from an assignment's age or disappearance.

After a successful read, save a dated report and a structured observation file in the history folder. For homework, record `checked_at`, student display name, school year, covered date range, coverage limitations, and entries with lesson date, lesson numbers, subject, teacher, original homework text, and attachment names. For all-updates checks, keep separate dated observations for grades, attendance/events, timetable changes, and messages, preserving each module's stable identifiers or visible date/subject/details needed to recognize changes. Preserve previous observations so changes can be audited. A partial read must be labeled partial and must not replace a complete baseline or justify a global “no changes” result. A module's first successful read establishes its baseline and is not proof that its records are new.

The initial baseline in workflow.md is a summary, not a verbatim snapshot. Compare it semantically on the first run; do not call wording differences new homework. If a difference cannot be established from that baseline, disclose the uncertainty and retain the new source text for later comparisons.

If a complete homework-only check finds no changes, report: `לא נמצאו שיעורי בית חדשים או שינויים מאז הבדיקה הקודמת.` If a complete all-updates check finds no changes, say that no new or changed updates were found and name the modules checked. If access failed, report the failure instead. Never claim no changes across modules that were inaccessible or only partially read. Save no credentials or session tokens.

## WhatsApp output

Use short Hebrew date and subject groups with single asterisks for WhatsApp bold. Include the reporting range and only enough emoji to aid scanning. Avoid tables. Separate classwork-only notes from actual assignments. Include a brief source limitation when relevant.

Example shape:

```text
📚 *עדכון שיעורי בית | 27/09/2026*

*27/9*
➗ *חשבון:* להשלים עמ׳ …
📖 *עברית:* שאלות … במחברת.
```

Preparing a WhatsApp- or Telegram-ready message does not include sending it. Sending is opt-in and requires the user to choose a channel and recipient, authorize sending in the one-off request or scheduled task, and have a connected, supported integration for that channel. Never guess a recipient or store login credentials, bot tokens, or session tokens in history. If the selected channel cannot be reached, return the prepared message and explain that it was not sent.

For a daily homework-only schedule, use: `Use the webtop skill to check for new or changed homework, prepare the Hebrew update, and save the observations for the next run.` For a daily all-updates schedule, use: `Use the webtop skill to check homework, grades, attendance and lesson events, timetable changes, and teacher messages for new or changed records since the previous check. Prepare one Hebrew update covering all changes, clearly list any module you could not check, and save separate observations for the next run.` To send it, append `Send this update via [WhatsApp or Telegram] to [the recipient I specify in this scheduled task]` after selecting one channel and recipient. Do not send if the channel or recipient is unspecified or its connected integration is unavailable; return the prepared message instead. Configure the schedule separately when requested and available; the user chooses the schedule time.
