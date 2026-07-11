# Changelog

## 0.3.0

- Replaces the generic L3 haze fallback with conditional depth mechanisms: light/exposure separation, distance-graded atmospheric perspective, or occlusion/scale recession.
- Distinguishes atmospheric perspective, physical fog, and a light-bearing medium; fog and volumetric shafts now require plausible-medium and motivated-light checks.
- Treats preset `smoke_haze` as conditional while preserving the public parameter ID.
- Prevents vacuum space and clean sealed environments from receiving automatic atmospheric haze.
- Updates the G2 sci-fi anti-slop clause and still-image adapter so depth preserves subject priority and background structure.
- Adds static regression validation for the new depth contract.

## 0.2.0

- Syncs image-only improvements from the local `cinematic-prompt-engine` v2.8.0.
- Adds `adapters/general.md` for GPT Image, Flux, Midjourney, and unspecified still-image models.
- Adds photography realism anchors: live-action still, camera-body anchor, optical bokeh, clean shadows, and tonal density.
- Adds noise-fuse handling for film stock names, fine grain, underexposure, and muddy shadow language.
- Adds softening-budget rules to prevent haze, grain, halation, diffusion, and shallow depth of field from stacking into smeared images.
- Adds multi-subject visual-priority rules and an image-variant workflow.
- Keeps the public edition image-only; video, i2v, character sheets, creature design sheets, and multi-shot video continuity remain out of scope.

## 0.1.0

- Initial public single-skill edition.
- Image-only cinematic prompt generation.
- LOOK transfer workflow.
- LOOK CARD workflow for fuzzy styles.
- Includes presets, params, recipes, and tiered anti-slop system.
- Adds demo gallery images for public README examples.
- Removes video, image-to-video, character, creature, and multi-skill routing scope.
