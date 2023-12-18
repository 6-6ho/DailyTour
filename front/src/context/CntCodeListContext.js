import { createContext, useContext, useState } from 'react';

const CntCodeListContext = createContext(  {cntCodeList: [], 
  setCntCodeList: () => {}} );

export const useCntCodeList = () => useContext(CntCodeListContext);

export const CntCodeListProvider = ({ children }) => {
    const [cntCodeList, setCntCodeList] = useState([null]);
  
    return (
      <CntCodeListContext.Provider value={{ cntCodeList, setCntCodeList }}>
        {children}
      </CntCodeListContext.Provider>
    );
  };


export default CntCodeListContext;