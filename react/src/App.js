import React from 'react';
import { BrowserRouter, HashRouter, Route } from 'react-router-dom';
import MainLayout from './components/MainLayout';
import './index.less';


export const DEV = (process.env.NODE_ENV === 'development');

let MyRouter;

if (DEV) {
  MyRouter = HashRouter;
} else {
  MyRouter = BrowserRouter;
}

export { MyRouter };

export default function () {
  return (
    <HashRouter>
      <Route path={'/'} component={MainLayout} />
    </HashRouter>
  );
}
