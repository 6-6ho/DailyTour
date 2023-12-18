import React, { lazy } from 'react';
import { Navigate } from 'react-router-dom';
import Loadable from '../layouts/full/shared/loadable/Loadable';


/* ***Layouts**** */
const FullLayout = Loadable(lazy(() => import('../layouts/full/FullLayout')));
const BlankLayout = Loadable(lazy(() => import('../layouts/blank/BlankLayout')));

/* ****Pages***** */
const Dashboard = Loadable(lazy(() => import('../views/dashboard/Dashboard')))
const CountryBoard = Loadable(lazy(() => import('../views/dashboard/components/CountryBoard')))
// const SamplePage = Loadable(lazy(() => import('../views/sample-page/SamplePage')))
// const Icons = Loadable(lazy(() => import('../views/icons/Icons')))
// const TypographyPage = Loadable(lazy(() => import('../views/utilities/TypographyPage')))
// const Shadow = Loadable(lazy(() => import('../views/utilities/Shadow')))

const Router = [
  {
    path: '/',
    element: <FullLayout />,
    children: [
      { path: '/', element: <Navigate to="/dashboard" /> },
      { path: '/dashboard', exact: true, element: <Dashboard /> },
      { path: '/country/:cntCode', exact:true, element: <CountryBoard/>}, 
      // { path: '/sample-page', exact: true, element: <SamplePage /> },
      // { path: '/icons', exact: true, element: <Icons /> },
      // { path: '/ui/typography', exact: true, element: <TypographyPage /> },
      // { path: '/ui/shadow', exact: true, element: <Shadow /> },
      { path: '*', element: <Navigate to="/auth/404" /> },
    ],
  },
  
];

export default Router;
