# Reference Workflow

## Reference Tag Syntax

Reference-binding notation is surface-specific. Resolve the active surface's exact token before writing a submission-ready prompt; do not derive a tag from the model family, a different provider, upload order, or these examples.

| Surface | Verified token convention | Rule |
| --- | --- | --- |
| fal Seedance API | `[Image1]`–`[Image9]`, `[Video1]`–`[Video3]`, `[Audio1]`–`[Audio3]` | Use the bracketed tokens documented by fal. Do not replace them with `@` mentions. |
| A surface that exposes `@` tokens in its own UI/API | The exact token supplied by that surface, such as `@Image1` | Preserve the token byte-for-byte. Do not translate, renumber, or change its delimiters. |
| Unknown or unverified surface | No assumed syntax | Preserve a user-provided token exactly. If none exists, keep reference roles in the plan and obtain the provider syntax before producing a final prompt. |

Write every resolved token with the job it does, never on its own: `<image-ref> as the first frame`, `follow <video-ref> for camera movement`, `<audio-ref> for background music`. The `@` examples elsewhere in this package illustrate role wording only; they are not universal syntax and must be rendered with the active surface's verified token convention.

## Asset Role Map

Before writing prompt prose, assign every uploaded asset a role. Role mapping prevents accidental transfer of identity, logos, scene ownership, or incompatible camera and motion instructions.

| Asset | Good Roles | Avoid |
|---|---|---|
| Image | identity, product, pose, costume, environment, first frame, last frame | asking it to define unseen motion |
| Video | motion, camera, pacing, blocking, timing, gesture rhythm | copying protected identity, logo, or scene ownership |
| Audio | rhythm, tempo, mood, ambience, delivery tone, music texture | assuming voice, song, or likeness authorization |
| Text brief | action, genre, camera plan, constraints | replacing concrete reference roles with vague mood words |

## Rules

- Preserve reference tags exactly.
- Give every reference one primary role before writing style language.
- Do not ask one reference to control incompatible roles unless the tradeoff is explicit.
- Use owned, licensed, public-domain, or clearly authorized references.
- Write what should transfer and what should not transfer.
- When authorization is unclear, transfer broad motion, tempo, mood, or production function rather than protected identity.
- Treat multimodal reference generation, video edit, video extend, and first/last-frame generation as separate tasks. They can share assets, but the prompt should name the active workflow.
- If audio and video references compete, make the video silent when audio timing must dominate, or state that the video controls camera/motion only and `<audio-ref>` controls tempo.
- In sequences, separate canonical references from accepted continuity sources: canonical identity/product references control immutable design, while accepted previous footage controls transient opening state.
- Never let a motion reference overwrite continuity locks, completed beats, reserved beats, or exact reference tags.

## Workflow-Specific Patterns

| Workflow | Use this wording | Avoid |
|---|---|---|
| Multimodal reference | `<image-ref> controls product identity; <video-ref> controls camera rhythm; <audio-ref> controls tempo only.` | `Use all references for style.` |
| Video edit | `<video-ref> is the source clip; preserve composition and timing, change only [lighting/background/VFX].` | Regenerating the whole concept from scratch. |
| Video extend | `<video-ref> is the previous clip; continue the same shot for [duration] and preserve last-frame continuity.` | Starting a new scene with no continuity anchor. |
| First/last frame | `<first-image-ref> is first frame; <last-image-ref> is final visual target; generate the continuous transition only.` | Asking the last frame to be only "mood." |
| Audio reference | `<audio-ref> controls tempo and energy; do not copy protected voice, song, or performance identity.` | Treating audio as authorization proof. |

## Role Examples

| Situation | Strong map |
|---|---|
| Product ad | `<image-ref> controls product identity; <audio-ref> controls tempo only.` |
| Motion transfer | `<video-ref> controls side-step choreography only; do not transfer performer, costume, room, or logo.` |
| Style reference | `<style-image-ref> controls warm bar atmosphere only; product identity remains from <identity-image-ref>.` |
| First-last frame | `<first-image-ref> is first frame; <last-image-ref> is target end frame; transition occurs through light sweep, not product deformation.` |
| Edit/extend | `<video-ref> is the source clip; preserve subject and camera path, replace only the failed lighting beat from 3s to 5s.` |

## Motion Transfer

Field-observed technique; test before promising results. Probably the most under-used reference capability: a donor video drives choreography or camera rhythm while an image keeps identity.

- Pair one donor `<video-ref>` with one identity anchor `<image-ref>`, and write the exclusion explicitly: `<video-ref> controls the choreography only - nothing of its appearance, performer, costume, room, or logo transfers.`
- Pick donor clips with one clear action, a clean silhouette, and a steady camera. Busy multi-person footage transfers noise, not motion.
- Mute the donor clip before upload unless its sound should drive timing; if it keeps sound, state which reference owns the clock.
- Transfers well: choreography, gesture timing, camera rhythm, blocking. Transfers poorly: fine hand detail, multi-person sync, facial performance.
- Use only owned, licensed, stock, mocap, rehearsal, or self-recorded donor footage; real-person donors transfer general motion only, never likeness.

## Template

`<image-ref> controls product identity. <video-ref> controls camera pace only. <audio-ref> controls tempo only. Preserve the subject from <image-ref>; do not copy characters, logos, music, voice, or environment from <video-ref>/<audio-ref>.`

## Sequence Transfer Template

`<accepted-video-ref> is the accepted previous clip and controls only the actual opening state, camera phase, motion phase, ambience, and environment arrangement. <identity-image-ref> controls canonical identity. Render both placeholders with the active surface's exact tags. Do not copy unrelated identity, costume, logo, or future action from any reference.`
