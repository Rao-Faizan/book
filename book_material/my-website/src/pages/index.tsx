import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';
import styles from './index.module.css';

function HomepageHeader() {
  const { siteConfig } = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <Heading as="h1" className="hero__title">
          {siteConfig.title}
        </Heading>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/module1/chapter1">
            Start Reading the Book 📘
          </Link>
        </div>
      </div>
    </header>
  );
}

function Feature({ title, description }) {
  return (
    <div className={clsx('col col--3')}>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

const FeatureList = [
  {
    title: 'Module 1: ROS 2 Foundation',
    description: 'Master the robotic nervous system. Learn Nodes, Topics, Services, and URDF modeling for humanoids.',
  },
  {
    title: 'Module 2: The Digital Twin',
    description: 'Simulate physics and optics using Gazebo and Unity. Bridge the gap between code and reality.',
  },
  {
    title: 'Module 3: AI-Robot Brain',
    description: 'Harness NVIDIA Isaac Sim and ROS for GPU-accelerated SLAM, Navigation, and Synthetic Data.',
  },
  {
    title: 'Module 4: VLA & Generative AI',
    description: 'Integrate GPT-4, Whisper, and CLIP to create Voice-Language-Action models for autonomous agents.',
  },
];

export default function Home(): JSX.Element {
  const { siteConfig } = useDocusaurusContext();
  return (
    <Layout
      title={`${siteConfig.title}`}
      description="A comprehensive guide to Physical AI and Humanoid Robotics.">
      <HomepageHeader />
      <main>
        <section className={styles.features}>
          <div className="container">
            <div className="row">
              {FeatureList.map((props, idx) => (
                <Feature key={idx} {...props} />
              ))}
            </div>
          </div>
        </section>
      </main>
    </Layout>
  );
}
