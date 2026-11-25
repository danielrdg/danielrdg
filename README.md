<p align="center">
  <img alt="Daniel Rodrigues: full-stack engineer, multi-agent orchestration. Porto Alegre, Brazil." src="assets/banner.svg" width="100%" />
</p>

<p align="center">
  <b>Full-stack software engineer working on multi-agent orchestration and AI harness engineering at Aegro.</b><br />
  Angular · TypeScript · Java · Spring Boot, with a background in the fiscal and tax domain.
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/danielrdgg"><img alt="LinkedIn" src="https://img.shields.io/badge/linkedin-danielrdgg-d9a441?style=flat-square&labelColor=3a130f" /></a>
  <a href="mailto:dani.araujo2002@gmail.com"><img alt="Email" src="https://img.shields.io/badge/email-dani.araujo2002%40gmail.com-ff5fa2?style=flat-square&labelColor=3a130f" /></a>
  <a href="https://github.com/danielrdg/maitre"><img alt="Now building: maître" src="https://img.shields.io/badge/now%20building-ma%C3%AEtre-ffd45c?style=flat-square&labelColor=3a130f" /></a>
</p>

<br />

<h2><img alt="about" src="assets/h-about.svg" height="48" /></h2>

I'm a full-stack software engineer based in Porto Alegre, Brazil, with hands-on experience across the stack: Angular and TypeScript on the front end, Java and Spring Boot on the back end, and PostgreSQL and MongoDB for data.

Today I work on multi-agent orchestration and the AI harness at Aegro: the engine, guardrails and workflows that let coding agents plan, implement, test and review changes across several codebases, with human approval at the points that matter.

<br />

<h2><img alt="experience" src="assets/h-experience.svg" height="48" /></h2>

**Aegro**: Software Engineer
- **Multi-agent orchestration and AI harness** (current). I design and build the agent workflows that take a ticket to a reviewed draft pull request, plus the tooling around them: planning, code review, error triage and support automation.
- **Fiscal and tax domain.** I built full-stack features in the fiscal area, with Java and Spring Boot services and Angular front ends.

<br />

<h2><img alt="education" src="assets/h-education.svg" height="48" /></h2>

**Software Engineering**, PUCRS (Pontifical Catholic University of Rio Grande do Sul), 2022–2026

<br />

<h2><img alt="now building" src="assets/h-building.svg" height="48" /></h2>

<a href="https://github.com/danielrdg/maitre"><img alt="maître: your agents' lounge. A terminal orchestrator for Claude Code agents." src="assets/maitre.svg" width="100%" /></a>

**[maître](https://github.com/danielrdg/maitre)** is a terminal orchestrator for Claude Code agents, with a pixel-art lounge where you watch them work. The plan: you write every request in one place, and each topic gets its own room, a real Claude Code session in its own git worktree, on the model that fits the job. A janitor will close idle rooms without ever losing work, and the one agent that needs you will ring the bell.

It's early: the first milestone, a demo of the lounge, is on its way. Open source, MIT.

<br />

<h2><img alt="selected work" src="assets/h-work.svg" height="48" /></h2>

Selected AI automation work. These are internal tools, so they're described by what they do, not how they're built.

<table>
  <tr>
    <td width="50%" valign="top">
      <img alt="" src="assets/i-ticket.svg" width="36" /><br />
      <b>Issue in, reviewed PR out.</b><br />
      An agent pipeline that reads a ticket, plans, implements, tests and reviews its own diff in the right codebase, then opens a draft pull request. One engine for backend, web and mobile codebases. A human approves the plan and the PR; it never merges.
    </td>
    <td width="50%" valign="top">
      <img alt="" src="assets/i-console.svg" width="36" /><br />
      <b>A "press play" cockpit.</b><br />
      A web console on top of that pipeline: pick an issue, read and edit the plan, approve it, and watch the run stream live.
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <img alt="" src="assets/i-moon.svg" width="36" /><br />
      <b>The long shift.</b><br />
      A long-running agent session: it takes open PRs to green, drafts reviews for a human to sign off, picks new work by explicit criteria and leaves a report at the end. It never merges, and anything irreversible waits for a human.
    </td>
    <td width="50%" valign="top">
      <img alt="" src="assets/i-spec.svg" width="36" /><br />
      <b>Spec-driven planning.</b><br />
      A planning flow that sizes itself to the task, from discovery to a written spec and a set of tasks, then hands execution to the agents above and keeps the outcome in view after launch.
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <img alt="" src="assets/i-broom.svg" width="36" /><br />
      <b>Error janitor.</b><br />
      Reads production error telemetry, dedupes by stack trace, separates user-facing bugs from noise, ranks what's left by frequency, impact and simplicity, and files ready-to-work issues.
    </td>
    <td width="50%" valign="top">
      <img alt="" src="assets/i-book.svg" width="36" /><br />
      <b>Support copilots.</b><br />
      Agents that write help-center articles by checking every step in a staging environment, and that investigate support tickets end to end, gathering read-only evidence before drafting the answer.
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <img alt="" src="assets/i-shield.svg" width="36" /><br />
      <b>PR risk triage</b> <sub>(co-built)</sub><br />
      A GitHub Action that labels every pull request low, medium or high risk from signals in the diff, so reviewers know where to look first.
    </td>
    <td width="50%" valign="top">
      <img alt="" src="assets/i-mask.svg" width="36" /><br />
      <b>Side project: <a href="https://github.com/danielrdg/elysium">elysium</a>.</b><br />
      The 24 voices of Disco Elysium as a Claude skill: one of them takes over Claude's voice for a few turns, then hands the mic to the next.
    </td>
  </tr>
</table>

<br />

<h2><img alt="stack" src="assets/h-stack.svg" height="48" /></h2>

<p>
  <img alt="Java" src="https://img.shields.io/badge/Java-3a130f?style=flat-square&logo=openjdk&logoColor=d9a441" />
  <img alt="Spring Boot" src="https://img.shields.io/badge/Spring%20Boot-3a130f?style=flat-square&logo=springboot&logoColor=d9a441" />
  <img alt="Angular" src="https://img.shields.io/badge/Angular-3a130f?style=flat-square&logo=angular&logoColor=d9a441" />
  <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-3a130f?style=flat-square&logo=typescript&logoColor=d9a441" />
  <img alt="PostgreSQL" src="https://img.shields.io/badge/PostgreSQL-3a130f?style=flat-square&logo=postgresql&logoColor=d9a441" />
  <img alt="MongoDB" src="https://img.shields.io/badge/MongoDB-3a130f?style=flat-square&logo=mongodb&logoColor=d9a441" />
  <img alt="Docker" src="https://img.shields.io/badge/Docker-3a130f?style=flat-square&logo=docker&logoColor=d9a441" />
  <img alt="Git" src="https://img.shields.io/badge/Git-3a130f?style=flat-square&logo=git&logoColor=d9a441" />
  <img alt="GitHub Actions" src="https://img.shields.io/badge/GitHub%20Actions-3a130f?style=flat-square&logo=githubactions&logoColor=d9a441" />
  <img alt="Claude Code" src="https://img.shields.io/badge/Claude%20Code-3a130f?style=flat-square&logo=claude&logoColor=ff5fa2" />
</p>

<br />

<p align="center">
  <img alt="A gold lattice border. Seating agents since 2026." src="assets/footer.svg" width="100%" />
</p>

<sub>Pixel art drawn in code for this profile. Lettering from Pixelify Sans and Silkscreen (SIL Open Font License), converted to shapes.</sub>
