import logo from './logo.svg';
import './App.css';
import {BrowserRouter, Route} from 'react-router-dom';
import Main from './main/main.tsx';
import ProductCreate from './admin/ProductCreate';
import Admin from './admin/Admin';
import ProductUpdate from './admin/ProductUpdate';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Route path='/' exact component={Main} />
        <Route path='/admin/products' exact component={Admin} />
        <Route path='/admin/products/create' exact component={ProductCreate} />
        <Route path='/admin/products/:id/edit' exact component={ProductUpdate} />
      </BrowserRouter>
    </div>
  );
}

export default App;
