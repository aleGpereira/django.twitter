import { request } from "../utils"

export const FETCH_TWEETS = "FETCH_TWEETS"
export const FETCH_TWEETS_SUCCESS = "FETCH_TWEETS_SUCCESS"
export const FETCH_TWEETS_ERROR400 = "FETCH_TWEETS_ERROR400"
export const FETCH_TWEETS_ERROR500 = "FETCH_TWEETS_ERROR500"
export const FETCH_TWEETS_FAILURE = "FETCH_TWEETS_FAILURE"
export function fetchTweets() {
  return function (dispatch) {
    let url = "http://localhost:8000/api/v1/tweets"
    dispatch({type: FETCH_TWEETS})
    return request(
      url, {},
      (json) => { dispatch({type: FETCH_TWEETS_SUCCESS, res: json}) },
      (json) => { dispatch({type: FETCH_TWEETS_ERROR400, res: json}) },
      (res) => { dispatch({type: FETCH_TWEETS_ERROR500, res: res}) },
      (ex) => { dispatch({type: FETCH_TWEETS_FAILURE, error: ex}) },
    )
  }
}