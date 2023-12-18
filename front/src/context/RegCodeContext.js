import { createContext, useContext, useState } from 'react';

const RegCodeContext = createContext();

export const useRegCode = () => useContext(RegCodeContext);

export const RegCodeProvider = ({ children }) => {
    const [regCode, setRegCode] = useState(null);
  
    return (
      <RegCodeContext.Provider value={{ regCode, setRegCode }}>
        {children}
      </RegCodeContext.Provider>
    );
  };


export default RegCodeContext;