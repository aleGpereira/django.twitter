import * as tweetsActions from "../actions/tweetsActions"

const initialState = {
  isLoadingTweets: false,
  tweets: undefined,
}

export default function twitter(state=initialState, action={}) {
  switch (action.type) {
  case tweetsActions.FETCH_TWEETS:
    return {...state, isLoadingTweets: true}
  case tweetsActions.FETCH_TWEETS_SUCCESS:
    return {...state, isLoadingTweets: false, tweets: action.res}
  case tweetsActions.FETCH_TWEETS_ERROR400:
  case tweetsActions.FETCH_TWEETS_ERROR500:
  case tweetsActions.FETCH_TWEETS_FAILURE:
    return {...state, isLoadingTweets: false}
  default:
    return state
  }
}