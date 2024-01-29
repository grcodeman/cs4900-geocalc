function func(vars) {
    return vars
}

function draw_canvas(points, lines, circles) {
    // Setup 2d canvas
    const canvas = document.getElementById("canvas");
    const ctx = canvas.getContext("2d");
    ctx.fillStyle = "#FF0000";
    canvas.height = canvas.width;

    // Draw lines
    var start_x_arr = lines.start_x;
    var start_y_arr = lines.start_y;
    var end_x_arr = lines.end_x;
    var end_y_arr = lines.end_y;

    ctx.strokeStyle = "black";
    for (let i = 0; i < start_x_arr.length; i++) {
        ctx.moveTo(start_x_arr[i], start_y_arr[i]);
        ctx.lineTo(end_x_arr[i], end_y_arr[i]);
        ctx.stroke();
    }

    // Draw circles
    var center_x_arr = circles.x;
    var center_y_arr = circles.y;
    var radius_arr = circles.radius;

    ctx.fillStyle = "red";
    for (let i = 0; i < center_x_arr.length; i++) {
        ctx.beginPath();
        ctx.ellipse(center_x_arr[i], center_y_arr[i], radius_arr[i], radius_arr[i], 0, 0, Math.PI * 2);
        ctx.fill();
    }

    // Draw points
    var x_arr = points.x;
    var y_arr = points.y;

    ctx.fillStyle = "blue";
    for (let i = 0; i < x_arr.length; i++) {
        ctx.beginPath();
        ctx.ellipse(x_arr[i], y_arr[i], 3, 3, 0, 0, Math.PI * 2);
        ctx.fill();
    }
}
