import './index.css'
import Navbar from './components/Navbar'
import Hero from './components/Hero'

function App() {
  return (
    <div className="app-container">
      <Navbar />
      <Hero />
      {/* We will add FoodieChat and RestaurantCards in Part 5 */}
    </div>
  )
}

export default App
