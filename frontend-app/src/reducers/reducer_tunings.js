import _ from 'lodash';
import { FETCH_TUNINGS, FETCH_TUNING, DELETE_TUNING } from '../actions';

export default function(state={}, action) {
  switch (action.type) {
    case DELETE_TUNING:
      return _.omit(state, action.payload);
    case FETCH_TUNING:
      return { ...state, [action.payload.data.id]: action.payload.data };
    case FETCH_TUNINGS:
      return _.mapKeys(action.payload.data, 'id');
    default:
      return state;
  }
}
