# Feature Specification: Module 2 - The Digital Twin (Gazebo & Unity)

**Feature Branch**: `2-digital-twin-module`
**Created**: 2025-12-07
**Status**: Draft
**Input**: Physical AI & Humanoid Robotics curriculum - Module 2 focusing on physics simulation and environment building

## Overview

Module 2 introduces students to robot simulation environments, focusing on creating high-fidelity digital twins of humanoid robots. Students learn to simulate physics, build environments, and integrate sensors in both Gazebo (for physics accuracy) and Unity (for visual fidelity). This module bridges the gap between pure software (Module 1) and AI-powered robotics (Module 3).

## User Scenarios & Testing

### User Story 1 - Introduction to Robot Simulation (Priority: P1)

Students need to understand why simulation is critical for robotics development, the concept of digital twins, and how simulation accelerates the development cycle while reducing costs and risks.

**Why this priority**: Foundational understanding of simulation principles before hands-on work. Students must understand sim-to-real gap, simulation advantages/limitations, and simulation workflows.

**Independent Test**: Students can explain simulation advantages over real robots, identify 3 types of simulation fidelity, and describe the sim-to-real pipeline.

**Acceptance Scenarios**:
1. **Given** a student completes Chapter 6, **When** asked about simulation benefits, **Then** they can list at least 5 advantages (cost, safety, speed, repeatability, scalability)
2. **Given** a student learns about digital twins, **When** presented with a robot design, **Then** they can explain what components need to be modeled
3. **Given** a student studies sim-to-real transfer, **When** reviewing simulation results, **Then** they can identify potential sources of reality gap

---

### User Story 2 - Gazebo Physics Simulation (Priority: P2)

Students need hands-on experience with Gazebo Fortress/Garden for accurate physics simulation. They must learn world building, spawning robots, configuring physics engines, and integrating ROS 2 with Gazebo.

**Why this priority**: Gazebo is the industry-standard ROS 2 simulator. Students need this before Unity because physics accuracy is more critical than visual fidelity for robotics.

**Independent Test**: Students create a custom Gazebo world, spawn their URDF humanoid from Module 1, apply forces, and verify realistic physics response.

**Acceptance Scenarios**:
1. **Given** a student completes Gazebo installation, **When** they launch Gazebo Fortress, **Then** the simulation environment loads without errors
2. **Given** a student creates a world file, **When** they add ground plane and obstacles, **Then** the world renders with correct physics properties
3. **Given** a student spawns their URDF robot, **When** gravity is enabled, **Then** the robot responds realistically to forces
4. **Given** a student configures ROS 2-Gazebo bridge, **When** they publish commands from ROS 2, **Then** the robot in Gazebo responds in real-time

---

### User Story 3 - Unity for High-Fidelity Rendering (Priority: P3)

Students learn to use Unity with Unity Robotics Hub for photorealistic rendering and human-robot interaction visualization. They integrate ROS 2 with Unity using TCP endpoints.

**Why this priority**: Unity provides superior visual quality for HRI (Human-Robot Interaction) scenarios. Lower priority than Gazebo because physics is more critical than visuals for robotics fundamentals.

**Independent Test**: Students import their robot into Unity, create a realistic indoor environment, and establish ROS 2 communication.

**Acceptance Scenarios**:
1. **Given** a student installs Unity Robotics Hub, **When** they create a new Unity project, **Then** ROS 2 packages are correctly configured
2. **Given** a student imports a URDF via Unity URDF Importer, **When** the model loads, **Then** all joints and links are correctly articulated
3. **Given** a student creates an indoor scene, **When** they apply lighting and materials, **Then** the scene achieves photorealistic quality
4. **Given** a student sets up ROS-TCP-Connector, **When** they send ROS 2 messages, **Then** Unity receives and visualizes them in real-time

---

### User Story 4 - Sensor Simulation (Priority: P4)

Students simulate robotic sensors (LiDAR, depth cameras, RGB cameras, IMUs, force-torque sensors) in both Gazebo and Unity. They learn sensor noise modeling, data visualization, and ROS 2 integration.

**Why this priority**: Sensor data is critical for perception but depends on having simulation environments set up first. Builds upon US2 and US3.

**Independent Test**: Students add a RealSense D435i camera and a LiDAR sensor to their robot, visualize point clouds in RViz2, and subscribe to sensor topics.

**Acceptance Scenarios**:
1. **Given** a student adds a camera sensor to URDF, **When** they spawn in Gazebo, **Then** image topics publish at correct frame rates
2. **Given** a student configures a LiDAR sensor, **When** obstacles are present, **Then** point cloud data accurately represents the environment
3. **Given** a student adds IMU to the robot, **When** the robot moves, **Then** IMU data (acceleration, gyroscope) matches motion
4. **Given** a student simulates sensor noise, **When** they compare noisy vs. clean data, **Then** they can explain noise model parameters

---

### User Story 5 - Sim-to-Real Transfer Techniques (Priority: P5)

Students learn domain randomization, reality gap analysis, and techniques for transferring policies trained in simulation to real robots. They understand calibration and fine-tuning strategies.

**Why this priority**: Advanced topic that synthesizes all previous learning. Critical for real-world deployment but requires complete understanding of simulation first.

**Independent Test**: Students apply domain randomization to their simulation, train a simple policy, and explain transfer strategies.

**Acceptance Scenarios**:
1. **Given** a student learns domain randomization, **When** they implement texture randomization, **Then** the environment varies across episodes
2. **Given** a student trains a policy in simulation, **When** they analyze performance, **Then** they can identify potential sim-to-real challenges
3. **Given** a student studies calibration techniques, **When** presented with sim-real differences, **Then** they can propose mitigation strategies

---

### Edge Cases
- Physics instability with complex humanoid models (high DOF, small contact patches)
- Real-time factor degradation with multiple sensors active
- URDF-to-Unity conversion errors (material properties, joint limits)
- ROS 2-Gazebo bridge latency issues
- GPU memory exhaustion with high-resolution sensors in Unity

## Requirements

### Functional Requirements

#### Chapter 6: Introduction to Robot Simulation
- **FR-001**: Chapter MUST explain the role of simulation in robotics development lifecycle
- **FR-002**: Chapter MUST define digital twin concept and its applications in robotics
- **FR-003**: Chapter MUST compare simulation vs. real robot development (cost, time, safety, scalability)
- **FR-004**: Chapter MUST explain sim-to-real gap and reality gap challenges
- **FR-005**: Chapter MUST introduce types of simulation fidelity (kinematic, dynamic, photorealistic)
- **FR-006**: Chapter MUST overview Gazebo (physics-first) vs. Unity (graphics-first) simulators
- **FR-007**: Chapter MUST explain simulation loops and real-time factors
- **FR-008**: Chapter MUST provide visual examples of simulation environments

#### Chapter 7: Gazebo Physics Simulation
- **FR-009**: Chapter MUST teach Gazebo Fortress/Garden installation on Ubuntu 22.04
- **FR-010**: Chapter MUST explain SDF (Simulation Description Format) for world building
- **FR-011**: Chapter MUST demonstrate creating world files with ground planes, lighting, and obstacles
- **FR-012**: Chapter MUST show how to spawn URDF robots in Gazebo using `ros2 run gazebo_ros spawn_entity.py`
- **FR-013**: Chapter MUST explain physics engines (ODE, Bullet, DART) and their trade-offs
- **FR-014**: Chapter MUST teach physics parameters (gravity, friction, contact properties)
- **FR-015**: Chapter MUST demonstrate Gazebo plugins for ROS 2 integration (`gazebo_ros_pkgs`)
- **FR-016**: Chapter MUST show how to apply forces and torques to robot links
- **FR-017**: Chapter MUST teach GUI navigation and camera controls in Gazebo
- **FR-018**: Chapter MUST explain real-time factor monitoring and performance optimization
- **FR-019**: Chapter MUST provide complete working example of humanoid walking in Gazebo

#### Chapter 8: Unity for High-Fidelity Rendering
- **FR-020**: Chapter MUST teach Unity Hub and Unity Editor installation (LTS version 2022.3+)
- **FR-021**: Chapter MUST explain Unity Robotics Hub architecture
- **FR-022**: Chapter MUST demonstrate ROS-TCP-Connector setup for ROS 2 communication
- **FR-023**: Chapter MUST show URDF import using Unity URDF Importer package
- **FR-024**: Chapter MUST teach creating realistic environments (indoor/outdoor scenes)
- **FR-025**: Chapter MUST explain Unity lighting systems (HDRP, URP)
- **FR-026**: Chapter MUST demonstrate materials and textures for photorealism
- **FR-027**: Chapter MUST show how to create interactive objects (doors, furniture)
- **FR-028**: Chapter MUST teach humanoid character animation integration
- **FR-029**: Chapter MUST explain Unity-ROS 2 message passing (publishers, subscribers)
- **FR-030**: Chapter MUST provide complete working example of robot in Unity scene

#### Chapter 9: Sensor Simulation
- **FR-031**: Chapter MUST explain sensor models (camera, LiDAR, depth, IMU, force-torque)
- **FR-032**: Chapter MUST demonstrate RGB camera simulation in Gazebo with `gazebo_ros_camera`
- **FR-033**: Chapter MUST demonstrate depth camera simulation (RealSense D435i equivalent)
- **FR-034**: Chapter MUST demonstrate 2D/3D LiDAR simulation with point cloud output
- **FR-035**: Chapter MUST demonstrate IMU simulation with noise models
- **FR-036**: Chapter MUST explain sensor noise modeling (Gaussian, salt-and-pepper)
- **FR-037**: Chapter MUST show how to visualize sensor data in RViz2
- **FR-038**: Chapter MUST teach sensor placement and field-of-view configuration
- **FR-039**: Chapter MUST demonstrate sensor simulation in Unity using Perception package
- **FR-040**: Chapter MUST explain sensor data formats and ROS 2 message types

#### Chapter 10: Sim-to-Real Transfer
- **FR-041**: Chapter MUST explain reality gap sources (physics approximation, sensor noise, actuation delays)
- **FR-042**: Chapter MUST teach domain randomization techniques (texture, lighting, physics parameters)
- **FR-043**: Chapter MUST demonstrate randomization implementation in Gazebo/Unity
- **FR-044**: Chapter MUST explain system identification for calibration
- **FR-045**: Chapter MUST teach sim-to-real validation metrics
- **FR-046**: Chapter MUST show fine-tuning strategies for real-world deployment
- **FR-047**: Chapter MUST explain progressive adaptation techniques
- **FR-048**: Chapter MUST provide case studies of successful sim-to-real transfers

### Key Entities
- **Gazebo Fortress/Garden**: Open-source 3D robotics simulator with accurate physics
- **Unity**: Game engine adapted for robotics with photorealistic rendering
- **SDF (Simulation Description Format)**: XML format for defining simulation worlds
- **Digital Twin**: Virtual replica of physical robot for testing and validation
- **ROS-TCP-Connector**: Bridge between ROS 2 and Unity
- **URDF Importer**: Unity package for importing robot models
- **Sensor Plugin**: Gazebo/Unity component that simulates sensor behavior
- **Domain Randomization**: Technique to vary simulation parameters for robust training
- **Real-time Factor**: Ratio of simulation time to wall-clock time

## Success Criteria

### Measurable Outcomes
- **SC-001**: Students can create a Gazebo world and spawn their URDF robot within 20 minutes
- **SC-002**: Students can establish ROS 2-Gazebo communication and control robot from command line within 15 minutes
- **SC-003**: Students can import robot into Unity and establish ROS-TCP connection within 30 minutes
- **SC-004**: Students can add and visualize camera and LiDAR sensors in RViz2 within 20 minutes
- **SC-005**: 85% of students successfully complete Module 2 assessment (simulation environment with multiple sensors)
- **SC-006**: Students can explain 3 domain randomization techniques when asked
- **SC-007**: Student simulations maintain >0.5 real-time factor with 5+ sensors active

### Learning Objectives Alignment
- **LO-001**: Master Gazebo for physics-accurate robot simulation
- **LO-002**: Understand Unity for photorealistic rendering and HRI scenarios
- **LO-003**: Implement and visualize sensor simulations
- **LO-004**: Prepare for Module 3 (Isaac Sim builds on simulation knowledge)
- **LO-005**: Understand sim-to-real challenges and mitigation strategies

## Assumptions
- Students have completed Module 1 (ROS 2 fundamentals and URDF)
- Students have Ubuntu 22.04 LTS with RTX GPU (4070 Ti or better)
- Module 2 is delivered in weeks 6-7 (2 weeks, ~6 contact hours)
- Students will use Gazebo Fortress or Garden (latest stable release)
- Unity LTS version 2022.3+ with Robotics Hub packages
- Students are familiar with 3D coordinate systems and transforms
- Jetson Orin Nano kits are available for hardware testing

## Dependencies

### External Dependencies
- Gazebo Fortress/Garden
- Unity Hub and Unity Editor 2022.3+
- Unity Robotics Hub packages (URDF Importer, ROS-TCP-Connector)
- ROS 2 Humble with `gazebo_ros_pkgs`
- RViz2 for sensor visualization
- Python packages: `numpy`, `scipy` for sensor processing

### Course Dependencies
- Prerequisites: Module 1 (ROS 2 and URDF knowledge required)
- Prepares for: Module 3 (Isaac Sim extends simulation concepts)

## Out of Scope
- Advanced Unity features (AR/VR, multiplayer)
- Custom physics engine development
- Gazebo Ignition (legacy version)
- Unreal Engine for robotics
- Full game development in Unity
- Deep reinforcement learning (covered in Module 3)
- ROS 1 Gazebo integration
- Web-based simulators (Webots)

## Risks and Mitigations

### Technical Risks
- **Risk**: Unity licensing confusion (free vs. paid tiers)
  - **Mitigation**: Provide clear guidance on Unity Personal (free for education)

- **Risk**: GPU compatibility issues with Unity HDRP
  - **Mitigation**: Test installation guides on target hardware; provide URP fallback

- **Risk**: Gazebo performance degradation with complex humanoids
  - **Mitigation**: Teach LOD (Level of Detail) techniques and simulation optimization

### Pedagogical Risks
- **Risk**: Students overwhelmed by two separate tools (Gazebo + Unity)
  - **Mitigation**: Clear separation - Gazebo for physics, Unity for visuals; optional Unity content

- **Risk**: Simulation abstraction hides real-world complexity
  - **Mitigation**: Emphasize reality gap throughout; lab sessions with real Jetson kits

## Open Questions
- Should Unity content be optional or required?
- What Unity LTS version offers best stability vs. features?
- Should we include Gazebo Harmonic (next LTS) or stick with Fortress?
