var slider = document.getElementById('slider-duration');
noUiSlider.create(slider, {
 start: [20, 120],
 connect: true,
 step: 1,
 orientation: 'horizontal', // 'horizontal' or 'vertical'
 range: {
   'min': 0,
   'max': 300
 },
 format: wNumb({
   decimals: 0
 })
});
    