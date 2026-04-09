import './Navbar.css';

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="navbar-container">
        <div className="logo brand-font">
          <span className="logo-icon">🍲</span>
          Lucknow<span className="highlight">Foodie</span>
        </div>
        <div className="nav-links">
          <a href="#home" className="nav-link active">Home</a>
          <a href="#restaurants" className="nav-link">Restaurants</a>
          <a href="#about" className="nav-link">About RAG</a>
        </div>
        <div className="nav-actions">
          <button className="btn-primary">Sign In</button>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
