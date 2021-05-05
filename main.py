from bokeh.plotting import figure, show, output_file

x = [1, 2, 3, 4, 5]
y = [4, 6, 2, 4, 3]

output_file('index.html')

# Add plot
p = figure(
  title='simple example',
  x_axis_label = 'X Axis',
  y_axis_label = 'Y Axis'
)

# Render glyph
p.line(x, y, legend_label='Test', line_width=3)

# Show results
show(p)