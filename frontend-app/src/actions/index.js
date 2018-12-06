import axios from 'axios';

export const FETCH_TUNINGS = 'fetch_tunings';
export const FETCH_TUNING = 'fetch_tuning';
export const CREATE_TUNING = 'create_tuning';
export const DELETE_TUNING = 'delete_tuning';
export const SELECT_TUNING = 'select_tuning';

const ROOT_URL = 'http://127.0.0.1:5000';

export function fetchTunings() {
  const request = axios.get(`${ROOT_URL}/tunings`);

  return {
    type: FETCH_TUNINGS,
    payload: request
  };
}

export function createTuning(values, callback) {
  const request = axios.post(`${ROOT_URL}/tuning`, values)
    .then(() => callback());
  return {
    type: CREATE_TUNING,
    payload: request
  };
}

export function fetchTuning(id) {
  const request = axios.get(`${ROOT_URL}/tuning/${id}`);

  return {
    type: FETCH_TUNING,
    payload: request
  }
}

export function deleteTuning(id, callback) {
  const request = axios.delete(`${ROOT_URL}/tuning/${id}`)
    .then(() => callback());

  return {
    type: DELETE_TUNING,
    payload: request
  }
}

export function selectTuning(id, callback) {
  const request = axios.post(`${ROOT_URL}/selected/${id}`)
    .then(() => callback());

  return {
    type: SELECT_TUNING,
    payload: request
  }
}
