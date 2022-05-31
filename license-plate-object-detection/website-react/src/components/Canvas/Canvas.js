import React from "react";

class Canvas extends React.Component {
  render() {
    return (
      <canvas
        className={this.props.className}
        ref={this.props.canvasRef}
        style={this.props.style}
      />
    );
  }
}
export default Canvas;


// const Canvas = React.forwardRef((props, ref) => {
//   return (
//     <canvas
//       className="size"
//       ref={ref}
//       width={props.width}
//       height={props.height}
//       style={props.style}
//     />
//   );
// });

