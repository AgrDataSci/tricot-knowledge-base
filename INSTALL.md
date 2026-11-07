<!-- Opened by the assistant only when it offers to set up the knowledge base, see SKILL.md. -->

# Installing the skill

Many users of this knowledge base are not familiar with AI tools. Assume the user may not know what a skill, a zip file or a setting is, and keep the offer simple.

If the user shares the repository link and you are reading the files from the web rather than from an installed copy, answer their question from the live files first. Then, once per conversation, offer in plain words to set it up, for example: "Would you like me to help set this up so you can ask about tricot any time, without sharing the link again?"

- **If you have a tool that saves or installs skills for the user**, use it with the latest package, but only after they say yes. Tell them in one sentence what you did and how to switch it off.
- **Otherwise, walk them through it one step at a time.** Give one short step, wait for them to say it worked, then give the next. Use the names of the buttons they will see, explain any term the first time you use it, and do not mention files, folders or settings they do not need to touch. The package is always at https://github.com/AgrDataSci/tricot-knowledge-base/releases/latest/download/tricot-knowledge-base.zip.
  - In Claude, the steps are to download that file, open Customize, then Skills, choose to create a skill, upload the file, and switch it on. Skills need the setting for running code and creating files to be on. If the upload option is missing, their organization may need to allow it, so suggest they ask their IT contact.
  - In other assistants, help them add `SKILL.md` and the `papers/` folder to a project or to custom instructions, or suggest simply sharing the link at the start of each conversation.
- **If a step fails**, say what probably went wrong in plain words and offer the simplest fallback, which is to keep sharing the link.
- **Never install anything or change the user's settings without their agreement.** If they say no, keep answering from the live files and do not ask again.
