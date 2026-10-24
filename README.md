# Digital Current Control and Energy Recovery for an Inductive Load

An electrical engineering project to design, simulate, and evaluate
a programmable current-controlled power supply with energy recovery.

## Project status

Early development.

The initial work focuses on mathematical modelling and simulation.
Hardware implementation is a possible later stage.

## What are we building?

We are building a power converter that controls current through a coil.

The current will follow a programmed cycle:

1. Ramp up to a chosen current.
2. Hold that current.
3. Ramp down to zero.
4. Rest before the next cycle.

During ramp-down, the converter will return some of the coil's stored
magnetic energy to a DC-link capacitor for reuse.

The first version will control positive current using both positive
and negative voltage. Current reversal is outside the initial scope.

## Motivation

Accelerator magnet power supplies combine current control, power
conversion, measurement, and protection. Some also recover magnetic
energy between operating cycles.

This project explores those principles using a simplified inductive
load at a scale suitable for undergraduate development.

It is an independent educational project, not affiliated with CERN.

## Objectives

- Develop and verify an RL load model.
- Generate a feasible current reference waveform.
- Implement PI current control with voltage limits and anti-windup.
- Compare PI control with PI plus feedforward.
- Model an H-bridge using averaged and switching representations.
- Recover magnetic energy into a DC-link capacitor.
- Evaluate losses, digital control effects, and protection behaviour.
- Document reproducible results and design limitations.

## System concept

The planned system includes:

- A DC supply with explicitly defined reverse-power behaviour.
- A DC-link capacitor.
- An H-bridge power converter.
- An RL load representing a coil.
- Current and DC-link voltage measurements.
- A digital current controller.
- Protection and excess-energy handling.

The source connection must allow the capacitor's voltage rise during
energy recovery to be represented correctly.

## Fundamental equations

RL load:

    v = L(di/dt) + Ri

Stored magnetic energy:

    E_L = 0.5 L i²

Stored capacitor energy:

    E_C = 0.5 C V²

Current error:

    e = i_reference - i_measured

Feedforward voltage:

    v_ff = R i_reference + L(di_reference/dt)

## Development roadmap

- [ ] Verify the numerical RL model against its analytical solution.
- [ ] Generate the ramp-hold-ramp-rest current reference.
- [ ] Implement PI current control.
- [ ] Add saturation and anti-windup.
- [ ] Implement feedforward and compare controller performance.
- [ ] Develop the averaged H-bridge model.
- [ ] Develop the switching model and examine current ripple.
- [ ] Model the DC-link capacitor and energy recovery.
- [ ] Size components and introduce realistic losses.
- [ ] Include sampling, measurement errors, and control delay.
- [ ] Implement operating states and fault responses.
- [ ] Run a reproducible validation campaign.
- [ ] Prepare a technical report and demonstration.
- [ ] Evaluate the feasibility of a hardware prototype.

## Validation plan

The project will evaluate:

- Agreement between analytical and numerical RL responses.
- Maximum and RMS current tracking error.
- Current ripple during the hold interval.
- Response to voltage saturation and load parameter changes.
- Maximum DC-link capacitor voltage.
- Energy returned during ramp-down.
- Losses and overall energy balance.
- Behaviour during stopping and selected fault conditions.

Every reported result will identify its assumptions, measurement
boundary, and whether it comes from simulation or hardware.

## Tools

The simulation platform and dependencies will be documented when
selected. Installation and execution instructions will be added
with the first runnable model.

## Results

No performance results are available yet.

Plots, controller comparisons, and energy calculations will be
added as the models are implemented and verified.

## References

- CERN SIRIUS converter family:
  https://section-mpc.web.cern.ch/sirius

- CERN Electrical Power Converters Group:
  https://sy-dep-epc.web.cern.ch/epc-group
