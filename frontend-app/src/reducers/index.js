import { combineReducers } from 'redux'
import { reducer as formReducer } from 'redux-form';
import TuningsReducer from './reducer_tunings';

const rootReducer = combineReducers({
  tunings: TuningsReducer,
  form: formReducer
});

export default rootReducer;
