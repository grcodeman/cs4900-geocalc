function func(vars) {
    return vars;
}

function draw_canvas(points, lines, circles, grid_size) {
    // Setup 2d canvas
    const canvas = document.getElementById("canvas");
    const ctx = canvas.getContext("2d");
    ctx.fillStyle = "#FF0000";
    canvas.height = canvas.width;

    // Calculate the length of 1 unit (d) based on grid_size
    var d = 500 / grid_size;
    console.log(d);

    // Draw Grid
    ctx.strokeStyle = "#c6c6ec";
    for (let i = 0; i < grid_size-1; i++) {
        ctx.beginPath();
        ctx.moveTo(0, d + (d * i));
        ctx.lineTo(500, d + (d * i));
        ctx.stroke();
    }
    for (let i = 0; i < grid_size-1; i++) {
        ctx.beginPath();
        ctx.moveTo(d + (d * i), 0);
        ctx.lineTo(d + (d * i), 500);
        ctx.stroke();
    }

    // Draw lines
    var start_x_arr = lines.start_x;
    var start_y_arr = lines.start_y;
    var end_x_arr = lines.end_x;
    var end_y_arr = lines.end_y;
    var highlighted_lines_arr = lines.is_highlighted;
    
    for (let i = 0; i < start_x_arr.length; i++) {
        if (highlighted_lines_arr[i]) {
            ctx.strokeStyle = "red";
        }
        else {
            ctx.strokeStyle = "black";
        }
        ctx.beginPath();
        ctx.moveTo(start_x_arr[i] * d, 500 - (start_y_arr[i] * d));
        ctx.lineTo(end_x_arr[i] * d, 500 - (end_y_arr[i] * d));
        ctx.stroke();
    }

    // Draw circles
    var center_x_arr = circles.x;
    var center_y_arr = circles.y;
    var radius_arr = circles.radius;

    ctx.fillStyle = "red";
    for (let i = 0; i < center_x_arr.length; i++) {
        ctx.beginPath();
        ctx.ellipse(center_x_arr[i] * d, 500 - (center_y_arr[i] * d), radius_arr[i] * d, radius_arr[i] * d, 0, 0, Math.PI * 2);
        ctx.fill();
    }

    // Draw points
    var x_arr = points.x;
    var y_arr = points.y;
    var highlighted_points_arr = points.is_highlighted;

    ctx.fillStyle = "blue";
    for (let i = 0; i < x_arr.length; i++) {
        if (highlighted_points_arr[i]) {
            ctx.fillStyle = "red";
        }
        else {
            ctx.fillStyle = "blue";
        }
        ctx.beginPath();
        ctx.ellipse(x_arr[i] * d, 500 - (y_arr[i] * d), 3, 3, 0, 0, Math.PI * 2);
        ctx.fill();
    }
}
