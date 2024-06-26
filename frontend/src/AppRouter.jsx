
import { ThemeProvider } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { useEffect, useState } from 'react';
import _ from 'lodash';

import './App.css';
import theme from './styles/theme.jsx';
import Api from './Api.jsx';

import Profile from './pages/profile.jsx'
import Logout from './pages/logout.jsx'


import Home from './pages/home.jsx';
import Variant from './pages/variant.jsx';
import About from './pages/about.jsx';
import TermsOfUse from './pages/terms.jsx';
import FAQ from './pages/faq.jsx';
import Contact from './pages/contact.jsx';

import AppLayoutWithNavigation from './AppLayoutWithNavigation.jsx';



function AppRouter() {
  //  const [user, setUser] = useState({email:"asdf@example.com"});
  const [user, setUser] = useState(null);

  useEffect(() => {
    Api.get('user', { json: true }).then((response) => {
      var user = _.get(response, 'user');
      if (_.isObject(user) && _.has(user, 'email') && user.email) {
        setUser(user);
      }
    });
  }, []);

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <BrowserRouter>
        <Routes>
          <Route path="/*" element={
            <AppLayoutWithNavigation user={user}>
              <Routes>
                <Route path="/" exact element={<Home user={user} />} />
                <Route path="/about" exact element={<About />} />
                <Route path="/terms" exact element={<TermsOfUse />} />
                <Route path="/faq" exact element={<FAQ />} />
                <Route path="/contact" exact element={<Contact />} />
                {user && <Route path="/variant/:varId" loader={({ params }) => { }} action={({ params }) => { }} element={<Variant />} />}
                {user && <Route path="/profile" element={<Profile user={user} />} />}
                {user && <Route path="/logout" element={<Logout user={user} setUser={setUser} />} />}
              </Routes>
            </AppLayoutWithNavigation>
          } />
        </Routes>
      </BrowserRouter>
    </ThemeProvider>
  )
}

export default AppRouter;