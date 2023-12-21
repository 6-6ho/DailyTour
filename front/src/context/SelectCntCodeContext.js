import { createContext, useContext, useState } from 'react';

const SelectCntCodeContext = createContext();

export const useSelectCntCode = () => useContext(SelectCntCodeContext);

export const SelectCntCodeProvider = ({ children }) => {
    const [selectCntCode, setSelectCntCode] = useState(null);
  
    return (
      <SelectCntCodeContext.Provider value={{ selectCntCode, setSelectCntCode }}>
        {children}
      </SelectCntCodeContext.Provider>
    );
  };


export default SelectCntCodeContext;