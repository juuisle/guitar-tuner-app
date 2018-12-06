import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { createStore, applyMiddleware } from 'redux';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import promise from 'redux-promise';

import reducers from './reducers';
import TuningsIndex from './components/tunings_index';
import TuningsNew from './components/tunings_new';
import TuningsShow from './components/tunings_show';

const createStoreWithMiddleware = applyMiddleware(promise)(createStore);

ReactDOM.render(
  <Provider store={createStoreWithMiddleware(reducers)}>
  <BrowserRouter>
    <div>
      <Switch>
        <Route path="/tunings/new" component={TuningsNew} />
        <Route path="/tunings/:id" component={TuningsShow} />
        <Route path="/" component={TuningsIndex} />
      </Switch>
    </div>
  </BrowserRouter>
  </Provider>
  , document.querySelector('.container'));



/*
*/
