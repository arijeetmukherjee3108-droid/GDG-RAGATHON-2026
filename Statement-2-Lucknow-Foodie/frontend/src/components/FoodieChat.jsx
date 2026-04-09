import { useState } from 'react';
import './FoodieChat.css';
import RestaurantCard from './RestaurantCard';
import axios from 'axios';

const FoodieChat = () => {
  const [query, setQuery] = useState('');
  const [budget, setBudget] = useState('');
  const [vegOnly, setVegOnly] = useState(false);
  const [loading, setLoading] = useState(false);
  const [response, setResponse] = useState(null);
  const [error, setError] = useState('');

  const handleSearch = async (e) => {
    e.preventDefault();
    if (!query.trim()) return;
    
    setLoading(true);
    setError('');
    
    try {
      const res = await axios.post('http://localhost:8000/api/recommend', {
        query,
        budget: budget ? parseInt(budget) : null,
        veg_only: vegOnly
      });
      
      setResponse(res.data);
    } catch (err) {
      setError('Failed to fetch recommendations! Make sure the FastAPI backend is running via `uvicorn app:app --reload`');
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="chat-section" id="restaurants">
      <div className="chat-container">
        <div className="search-panel">
          <h2>Find Your Perfect Spot</h2>
          <form className="search-form" onSubmit={handleSearch}>
            <div className="input-group">
              <input 
                type="text" 
                placeholder="E.g., Suggest a cozy cafe near Gomti Nagar with great desserts..." 
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                autoFocus
              />
            </div>
            
            <div className="filters">
              <input 
                type="number" 
                placeholder="Max Budget (₹)" 
                value={budget}
                onChange={(e) => setBudget(e.target.value)}
                className="filter-input"
              />
              <label className="checkbox-label">
                <input 
                  type="checkbox" 
                  checked={vegOnly} 
                  onChange={(e) => setVegOnly(e.target.checked)}
                />
                Veg Only
              </label>
              <button type="submit" className="search-btn" disabled={loading}>
                {loading ? <span className="loader"></span> : 'Search'}
              </button>
            </div>
          </form>
        </div>

        {error && <div className="error-message">{error}</div>}

        {response && (
          <div className="results-panel fade-in">
            <div className="llm-response">
              <div className="ai-badge">🤖 AI Recommendation</div>
              <div className="ai-text" dangerouslySetInnerHTML={{ __html: response.recommendation.replace(/\n/g, '<br/>') }} />
            </div>
            
            {response.raw_results && response.raw_results.length > 0 && (
              <div className="cards-grid">
                {response.raw_results.map((rest, idx) => (
                  <RestaurantCard key={idx} restaurant={rest} />
                ))}
              </div>
            )}
          </div>
        )}
      </div>
    </section>
  );
};

export default FoodieChat;
