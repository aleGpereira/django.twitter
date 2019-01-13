import React from "react"

export default class TweetList extends React.Component {
  render() {
    let {tweets} = this.props
    let repoNodes = []
    tweets.forEach((item, index) => {
      let node = (
        <div key={item.id}>
            <h3> {item.author}</h3>
            <div> {item.text}</div>
        </div>
      )
      repoNodes.push(node)
    })

    return (
      <div>{repoNodes}</div>
    )
  }
}