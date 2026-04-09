import './RestaurantCard.css';

const RestaurantCard = ({ restaurant }) => {
  return (
    <div className="restaurant-card">
      <div className="card-image-placeholder">
        <span className="card-rating">⭐ {restaurant.rating}</span>
      </div>
      <div className="card-content">
        <h3 className="card-title">{restaurant.name}</h3>
        <p className="card-area">{restaurant.area}</p>
        <div className="card-details">
          <span className="card-price">₹{restaurant.price_range} for two</span>
          <span className={`card-type ${restaurant.veg ? 'veg' : 'non-veg'}`}>
            {restaurant.veg ? '🟩 Veg' : '🟥 Non-Veg'}
          </span>
        </div>
      </div>
    </div>
  );
};

export default RestaurantCard;
