import './Hero.css';

const Hero = () => {
  return (
    <section className="hero-section">
      <div className="hero-content">
        <h1 className="hero-title">
          Hungry? Let AI Find Your <br/>
          <span className="gradient-text">Perfect Lucknow Vibe</span>
        </h1>
        <p className="hero-subtitle">
          Tired of endless scrolling? Ask our RAG-powered chatbot to find the best Tunday Kababi, budget biryanis, or aesthetic cafes near IIIT Lucknow.
        </p>
      </div>
      <div className="hero-graphics">
        <div className="floating-card c1">🍗 Best Biryani</div>
        <div className="floating-card c2">☕ Cozy Cafes</div>
        <div className="floating-card c3">💸 Budget Friendly</div>
      </div>
    </section>
  );
};

export default Hero;
