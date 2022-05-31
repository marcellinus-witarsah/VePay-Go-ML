import React from "react";
class Camera extends React.Component {
  render() {
    return (
      <video
        className={this.props.className}
        autoPlay
        playsInline
        muted
        ref={this.props.videoRef}
        id="frame"
        // width={this.props.width}
        // height={this.props.height}
      />
    );
  }
}
export default Camera;
