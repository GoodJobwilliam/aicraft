# Team Trial Follow-up Playbook

Manual, zero-budget process for turning a public trial request into a real product decision. Use only information the applicant chooses to share in the issue; never ask for source code, secrets, or private credentials.

## Service level

- Reply in the issue thread within 24 hours when practical.
- Acknowledge the team's stated language, workflow, pain, role, and decision window.
- Give one concrete next step, not a product tour.
- Close the loop after seven days if there is no response.

## Reply sequence

### 1. First reply

Thank them, restate the problem in one sentence, and point to the 10-minute trial kit. Ask them to report three things: what it caught, which rule they would share, and what was noisy.

### 2. Trial review

If they report a real finding, ask whether the same rule should run in every repository and whether CI should block on it. If they report noise, ask for the rule intent and desired severity; do not ask for private code.

### 3. Offer selection

- **Rules only**: point to the free config workflow first; offer the `$49` Team Rules Pack when the team wants the validated multi-language profiles, CI templates, and prompts.
- **Rules-only checkout**: after the team confirms the pack solves the stated problem, send the [Creem checkout link](https://creem.io/checkout/prod_6Z3S3jGNPsCyRSqNi397ZY/ch_6wLlsvodjjvKq73eBpZCP0) and record the payment only after Creem confirms it.
- **Ongoing maintenance**: offer Starter at `$19/month` or `$190/year` for up to 3 engineers, or Team Pilot at `$99/month` or `$990/year` for up to 10 engineers with the first-30-day CI and tuning reviews. Confirm exact scope and start date before charging.
- **No decision yet**: leave the free server and trial kit as the next step; do not push a checkout link.

## Copy-ready replies

### First reply (English)

Thanks for sharing the context. I understand that **[pain]** is affecting **[workflow]** for a **[team size]-person [language]** team. Please run the [10-minute trial kit](https://aicraft.vip/trial.html) and reply by issue or email with: (1) what it caught, (2) which rule you would share across repositories, and (3) what was noisy. No source code or secrets are needed.

### Trial review (English)

That is useful signal. Should this rule run in every repository, and should CI block on it? If the rule set is the main need, the one-time `$49` Team Rules Pack includes validated Python/JS/TS/Go/Java profiles, CI templates, and review prompts. If keeping the rules current is the bigger problem, Starter is `$19/month` or `$190/year` for up to 3 engineers, while Team Pilot is `$99/month` or `$990/year` for up to 10 engineers with CI and tuning support; we confirm scope and start date before charging.

### 首次回复（中文）

感谢你补充背景。我理解 **[痛点]** 正在影响 **[流程]**，团队规模约 **[人数]**，主要使用 **[语言]**。请先运行[10 分钟自助试用包](https://aicraft.vip/trial.zh.html)，然后在 issue 或邮件中回复三点：1）发现了什么；2）哪些规则希望所有仓库共享；3）哪些结果属于误报。不需要提供源代码或密钥。

### 试用复盘（中文）

这个反馈很有价值。你们是否希望这条规则在每个仓库都执行？CI 是否应该在命中时阻止合并？如果主要需求是现成规则，$49 Team Rules Pack 包含 Python/JS/TS/Go/Java 规则档案、CI 模板和审查提示词；如果主要问题是持续维护，Starter 是最多 3 人的 $19/月或 $190/年，Team Pilot 是最多 10 人的 $99/月或 $990/年，后者包含 CI 和调优支持。收费前会先确认范围和开始时间。

### Follow-up timing

- Set `next_follow_up` to 2 business days after the first reply.
- Set it to 7 days after a trial result if the team has not chosen an offer.
- Stop after the close-the-loop message unless the applicant reopens the conversation.

## Evidence thresholds

Record these in `OUTREACH_LOG.csv`:

- **Qualified reply**: describes a recurring review pain and answers the workflow questions.
- **Team test**: runs the sample or a real non-confidential test and reports an outcome.
- **Paid signal**: explicitly says they would buy the `$49` pack or consider Team Updates Starter/Team Pilot at one of the stated prices; record the selected tier in `offer_tier`.
- **Pre-commitment**: names a target start month and accepts the stated scope and price, subject to the final checkout link.
- **Customer**: payment is confirmed in Creem; a message or intent does not count as revenue.

## Revenue math

The `$2,000` MRR target can be reached with 21 Team Pilot customers at `$99/month` (`$2,079` MRR). Starter remains a low-friction option for smaller teams. Annual plans are tracked as recurring revenue using their monthly equivalent (`$990/year` = `$82.50` MRR; `$190/year` = `$15.83` MRR per customer). Team Rules Pack purchases add one-time revenue but do not count toward MRR.

Do not treat one-time `$49` purchases as MRR. Track one-time revenue and recurring revenue separately.

## Weekly review

Every seven days, count: contacts, qualified replies, team tests, paid signals, pre-commitments, Team Rules Pack sales, Team Updates subscribers, one-time revenue, and MRR. Update the offer only when several conversations show the same pain.
