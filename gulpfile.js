(function(){
    'use strict';

    const gulp = require('gulp');
    const sass = require('gulp-sass');
    const autoprefixer = require('gulp-autoprefixer');
    const sourcemaps = require('gulp-sourcemaps');
    const gncd = require('gulp-npm-copy-deps');

    gulp.task('sass', function () {
        return gulp.src('./lib/sass/**/*.sass')
            .pipe(sourcemaps.init())
            .pipe(sass().on('error', sass.logError))
            .pipe(autoprefixer({
                browsers: ['last 5 versions'],
                cascade: false
            }))
            .pipe(sourcemaps.write())
            .pipe(gulp.dest('./spin/static/css'));
    });

    gulp.task('sass:watch', function () {
        gulp.watch('./lib/sass/**/*.sass', ['sass']);
    });

    gulp.task('copy-dependencies', function () {
        return gncd('./node_modules', './spin/static/vendor');
    });

    gulp.task('build', ['copy-dependencies', 'sass']);

    gulp.task('default', ['copy-dependencies', 'sass','sass:watch']);


}());
