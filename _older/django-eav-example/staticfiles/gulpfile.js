// usage: `gulp build` or `gulp build --watch`

'use strict'

var gulp = require('gulp')
var webpack = require('webpack')
var autoprefixer = require('autoprefixer')
var watch = require('gulp-watch')
var livereload = require('gulp-livereload')
var gutil = require('gulp-util')

var webpackConfig = {
  entry: './index.es6',
  
  output: {
    path: '.',
    filename: 'index.js',
  },
  
  module: {
    loaders: [
      {
        test: /\.es6$/,
        loader: 'babel',
        query: {presets: ['es2015', 'stage-0']},
      },
      
      {test: /\.less$/, loader: 'style!css!postcss!less'},
    ],
  },
  
  postcss: function postcss() {
    return [autoprefixer({browsers: ['last 2 versions']})]
  },
}


if (gutil.env.watch) {
  livereload.listen()
  gulp.task('build', ['_build-watch'])
} else {
  gulp.task('build', ['_build'])
}



gulp.task('_build', function(cb) {
  webpack(webpackConfig, function(err, stats) {
    if (err) cb(new gutil.PluginError('webpack', err))
    else gutil.log('[webpack]', stats.toString()); cb()
  })
})


gulp.task('_build-watch', function(cb) {
  var watcherOpts = undefined // all defaults
  
  webpack(webpackConfig).watch(watcherOpts, function(err, stats) {
    if (err) {
      cb(new gutil.PluginError('webpack', err))
    } else {
      gutil.log('[webpack]', stats.toString())
      livereload.reload()
    }
  })
})
