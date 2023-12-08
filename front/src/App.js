import { CssBaseline, ThemeProvider } from '@mui/material';
import { useRoutes } from 'react-router-dom';
import Router from './routes/Router';
import { useState } from 'react';
import { baselightTheme } from "./theme/DefaultColors";
import Attractions from './views/dashboard/components/Attractions';
import Accomodations from './views/dashboard/components/Accomodations';
import { RegCodeProvider } from './context/RegCodeContext';

function App() {
  const routing = useRoutes(Router);
  const theme = baselightTheme;
  const [regCode, setRegCode] = useState(null);

  return (
    <ThemeProvider theme={theme}>

      <CssBaseline />
      <RegCodeProvider>
          {routing}
      </RegCodeProvider>

    </ThemeProvider>
  );
}

export default App;
