import React from "react"
import Radium from "radium"

import { connect } from "react-redux"

import * as tweetsActions from "../actions/tweetsActions"
import Headline from "../components/Headline"
import TweetList from "../components/TweetList"

@connect(state => ({
  twitter: state.twitter,
}))
@Radium
export default class TwitterStuffContainer extends React.Component {
  componentDidMount() {
    let {dispatch, twitter} = this.props
    if (!twitter.isLoadingTweets && twitter.tweets === undefined) {
      dispatch(tweetsActions.fetchTweets())
    }
  }

  renderLoading() {
    return (
      <div className="container">
        <div className="row">
          <div className="col-sm-12">
            Loading tweets...
          </div>
        </div>
      </div>
    )
  }

  render() {
    let {twitter} = this.props
    if (twitter.isLoadingTweets || twitter.tweets === undefined) {
      return this.renderLoading()
    }
    return (
      <div className="container">
        <div className="row">
          <div className="col-sm-12">
            <Headline>Got my Home tweets!</Headline>
            {twitter.tweets !== undefined &&
              <TweetList tweets={twitter.tweets} />
            }
          </div>
        </div>
      </div>
    )
  }
}