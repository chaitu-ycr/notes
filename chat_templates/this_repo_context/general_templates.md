# 🤖 Copilot Chat Context Template

Use this template when starting new conversations with GitHub Copilot for documentation work.

---

## 📋 Template: General Documentation Work

```
I'm working on [TOPIC] documentation for a learning repository focused on 
[DOMAIN: automotive development / Python programming / testing].

The repository uses a creative, practical style:
- Lead with funny/real-world analogies
- Show working code examples immediately after concepts
- Include "gotchas" and edge cases with humor
- Less theory, more practice
- Always use Markdown

The structure is [LOCATION in repo]. I need help with:
[SPECIFIC TASK: explaining concept / creating example / debugging issue]

Please follow this style:
1. Hook with a creative analogy or scenario
2. Show practical code (not just theory)
3. Explain edge cases and common mistakes
4. Use emojis for visual scanning
5. Keep it professional yet fun
```

---

## 📋 Template: Python Content

```
I'm creating Python documentation for [TOPIC: e.g., "decorators", "pytest", "multithreading"].

Context:
- Repository: Learning hub with automotive + Python focus
- Target audience: Software engineers learning Python
- Style: Practical examples, funny explanations, creative tone
- Location: Will be in `/python/basics/` or `/python/usecases/`
- Format: Markdown with embedded code

Please create/explain:
[YOUR REQUEST]

Style requirements:
- Start with a funny/relatable analogy
- Show working, copy-paste ready code
- Include common mistakes developers make
- Add a "gotcha" or advanced pattern
- Use emojis (🎯, 🚀, ⚠️, 🔥, 🐛)
```

---

## 📋 Template: Automotive Protocol Content

```
I'm documenting [PROTOCOL: CAN / UDS / DoIP / ASPICE].

Context:
- For: Automotive engineers and developers
- Real-world scenario: [DESCRIBE the communication/process]
- Current understanding: [WHERE YOU ARE]
- Need help with: [WHAT YOU NEED]

Style for automotive:
- Explain with real ECU scenarios
- Show hex values and bit layouts
- Include timing diagrams or message flows
- Share debugging stories/gotchas
- Link to Vector tools when relevant

Please [CREATE/EXPLAIN]: [YOUR REQUEST]
```

---

## 📋 Template: Code Example or Usecase

```
I'm creating a usecase example for [TOOL/FRAMEWORK: pytest / streamlit / pandas / etc.].

Repository context:
- This is in `/python/usecases/`
- Style: Practical, funny, real-world examples
- Audience: Developers who learn by doing

I need:
- Installation/setup steps
- Basic usage (simple, relatable example)
- Advanced patterns or gotchas
- Common mistakes and how to fix them
- Real-world scenario where this matters

Please create an example that:
1. Shows the simplest working version first
2. Builds up to real-world usage
3. Includes debugging tips
4. Is funny/engaging but professional
```

---

## 📋 Template: Fixing/Reviewing Existing Content

```
I'm reviewing/improving documentation in this repo.

Current file: [PATH/TO/FILE.md]
Issue: [WHAT'S WRONG / WHAT NEEDS IMPROVEMENT]
Context: [ADDITIONAL INFO]

The repo style is:
- Creative + Professional
- Practical examples over theory
- Funny/engaging analogies
- Clear structure, scannable
- Automotive or Python focus

Please [SUGGEST CHANGES / FIX / IMPROVE]:
[DESCRIBE WHAT YOU WANT]
```

---

## 📋 Template: Automotive Project Deep Dive

```
I'm documenting a project structure for [PROJECT: ADAS / ABS / BMS / IPC].

Components involved:
- [ECU/Component 1]: [Function]
- [ECU/Component 2]: [Function]

I need help creating documentation that covers:
1. Project overview and architecture
2. Key protocols/communication (CAN, UDS, DoIP)
3. Real-world implementation examples
4. Debugging and testing strategies
5. Common pitfalls and how to handle them

Repository style guide applies (creative, practical, real-world focus).
Should be in `/projects/[PROJECT_NAME]/`

Please help with: [SPECIFIC REQUEST]
```

---

## 💡 Pro Tips for Better Copilot Results

### 1. **Be Specific About Location**
```
✅ Good: "For /python/basics/005_list.md - I need to explain list comprehensions"
❌ Vague: "I need to explain list comprehensions"
```

### 2. **Provide Context Examples**
```
✅ Show existing similar files: "Like how 001_variables.md uses analogies..."
✅ Show your audience: "For engineers learning Python, not CS students"
```

### 3. **Describe Your Audience**
```
✅ Specific: "Automotive ECU developers who know CAN but not UDS"
❌ Vague: "Software engineers"
```

### 4. **Ask for Style Elements**
```
✅ "Include a funny analogy like 'CAN is like...' and show actual hex values"
✅ "Emojis for scannability: 🎯 for key concepts, ⚠️ for gotchas"
```

### 5. **Clarify Your Goals**
```
✅ "Help beginners understand without overwhelming them"
✅ "This should take 5 minutes to read"
✅ "Include 3-4 practical examples"
```

---

## 🎯 Common Requests & Quick Templates

### "Create a tutorial on [TOPIC]"
```
Create a [TOPIC] tutorial for /python/basics/ that:
- Starts with a funny real-world analogy
- Shows basic example first (5 lines max)
- Explains with inline comments
- Includes gotchas section
- Provides advanced usage pattern
```

### "Debug why this isn't clear"
```
Analyze this content for clarity:
[PASTE CONTENT]

Issues: [LIST ISSUES]

Fix it for:
- First-time learners in this domain
- Readable/scannable format
- Practical over theoretical
- Automotive/Python context (whichever applies)
```

### "Explain this concept"
```
Explain [CONCEPT] for [AUDIENCE] in the style of this repo:
[EXISTING SIMILAR FILE/SECTION]

Should be suitable for: [LOCATION/PURPOSE]
```

---

## 📞 When You're Stuck

If Copilot's response doesn't match your repo style:

1. **Provide a reference:** "Like how `/CAN/readme.md` starts with..."
2. **Be more specific:** "I need MORE code, LESS theory"
3. **Give examples:** "Show me 3-4 practical scenarios"
4. **Clarify tone:** "Make this funny but still professional"
5. **Point to what you like:** "I like the approach in `/python/usecases/pytest.md`"

---

## 🎉 You're Ready!

Now you have templates that will help Copilot understand your repo's personality and produce content that fits perfectly with your existing documentation style.

**Key Takeaway:** The more context you give Copilot about your audience, style, and goals, the better it will help you create amazing documentation.

---

*Remember: This repo celebrates practical learning through creativity!*

