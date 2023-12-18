import { CssBaseline, ThemeProvider } from '@mui/material';
import { useRoutes } from 'react-router-dom';
import Router from './routes/Router';
import { useState } from 'react';
import { baselightTheme } from "./theme/DefaultColors";
import { RegCodeProvider } from './context/RegCodeContext';
import { CntCodeListProvider } from './context/CntCodeListContext';

function App() {
  const routing = useRoutes(Router);
  const theme = baselightTheme;
  // const [regCode, setRegCode] = useState(null);
  // const [cntCodeList, setCntCodeList] = useState(null);

  return (
    <ThemeProvider theme={theme}>

      <CssBaseline />
      <RegCodeProvider>
        <CntCodeListProvider>
          
            {routing}
          
        </CntCodeListProvider>
        </RegCodeProvider>
    </ThemeProvider>
  );
}

export default App;
