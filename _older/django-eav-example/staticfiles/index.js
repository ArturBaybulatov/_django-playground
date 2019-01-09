/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};

/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {

/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId])
/******/ 			return installedModules[moduleId].exports;

/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			exports: {},
/******/ 			id: moduleId,
/******/ 			loaded: false
/******/ 		};

/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);

/******/ 		// Flag the module as loaded
/******/ 		module.loaded = true;

/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}


/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;

/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;

/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";

/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(0);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/***/ function(module, exports, __webpack_require__) {

	/* WEBPACK VAR INJECTION */(function(global) {'use strict';

	__webpack_require__(1);

	__webpack_require__(5);

	global.g = global;

	var $$ = g.$$ = myUtil;

	var MONTHS = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'];

	g.DEBUG = false;

	var app = angular.module('app', ['ui.bootstrap', 'ui.select', 'checklist-model', 'ui.bootstrap-slider']);

	app.config(['$interpolateProvider', '$httpProvider', function ($interpolateProvider, $httpProvider) {
	  $interpolateProvider.startSymbol('{(');
	  $interpolateProvider.endSymbol(')}');

	  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
	  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
	}]);

	app.service('util', function util() {
	  var s = this;

	  s.formatDate = function formatDate(dateStr) {
	    var date = new Date(dateStr);
	    return 'Добавлено ' + date.getDate() + '.' + MONTHS[date.getMonth()] + '.' + date.getFullYear();
	  };

	  s.readableAdvertGender = function readableAdvertGender(advertGender) {
	    return { boys: 'Мальчик', girls: 'Девочка' }[advertGender];
	  };

	  s.remove = function remove(item, coll) {
	    $$.splice(1, coll.indexOf(item), coll);
	  };
	});

	app.run(['$rootScope', 'util', '$timeout', '$http', function run(s, util, $timeout, $http) {
	  s._ = _;
	  s.$$ = $$;
	  s.Math = Math;
	  s.util = util;

	  global.$http = $http; // Debug

	  $timeout(function () {
	    $('.-icheck.-icheck-default input[type="checkbox"]').icheck({ checkboxClass: 'icheckbox_square' });
	    $('.-icheck.-icheck-blue input[type="checkbox"]').icheck({ checkboxClass: 'icheckbox_square-blue' });

	    $('.-icheck input[type="radio"].-icheck-default').icheck({ radioClass: 'iradio_square' });
	    $('.-icheck input[type="radio"].-icheck-white').icheck({ radioClass: 'iradio_square' });
	    $('.-icheck input[type="radio"].-icheck-violet').icheck({ radioClass: 'iradio_square-purple' });
	    $('.-icheck input[type="radio"].-icheck-red').icheck({ radioClass: 'iradio_square-red' });
	    $('.-icheck input[type="radio"].-icheck-green').icheck({ radioClass: 'iradio_square-green' });
	    $('.-icheck input[type="radio"].-icheck-gray').icheck({ radioClass: 'iradio_square-grey' });
	    $('.-icheck input[type="radio"].-icheck-blue').icheck({ radioClass: 'iradio_square-blue' });
	    $('.-icheck input[type="radio"].-icheck-yellow').icheck({ radioClass: 'iradio_square-yellow' });
	    $('.-icheck input[type="radio"].-icheck-cyan').icheck({ radioClass: 'iradio_square' });
	  });
	}]);

	function getLocationTree(locations, location) {
	  var subway = undefined,
	      district = undefined,
	      town = undefined,
	      region = undefined;
	  var subways = undefined,
	      districts = undefined,
	      towns = undefined,
	      regions = undefined;

	  if (location && location.level === 4) {
	    subway = location;
	    district = _.find({ id: subway.parent }, locations);
	    town = _.find({ id: district.parent }, locations);
	    region = _.find({ id: town.parent }, locations);

	    subways = _.filter(function (l) {
	      return l.level === 4 && l.parent === district.id;
	    }, locations);
	    districts = _.filter(function (l) {
	      return l.level === 3 && l.parent === town.id;
	    }, locations);
	    towns = _.filter(function (l) {
	      return l.level === 2 && l.parent === region.id;
	    }, locations);
	    regions = _.filter(function (l) {
	      return l.level === 1;
	    }, locations);
	  } else if (location && location.level === 3) {
	    district = location;
	    town = _.find({ id: district.parent }, locations);
	    region = _.find({ id: town.parent }, locations);

	    subways = _.filter(function (l) {
	      return l.level === 4 && l.parent === district.id;
	    }, locations);
	    districts = _.filter(function (l) {
	      return l.level === 3 && l.parent === town.id;
	    }, locations);
	    towns = _.filter(function (l) {
	      return l.level === 2 && l.parent === region.id;
	    }, locations);
	    regions = _.filter(function (l) {
	      return l.level === 1;
	    }, locations);
	  } else if (location && location.level === 2) {
	    town = location;
	    region = _.find({ id: town.parent }, locations);

	    districts = _.filter(function (l) {
	      return l.level === 3 && l.parent === town.id;
	    }, locations);
	    towns = _.filter(function (l) {
	      return l.level === 2 && l.parent === region.id;
	    }, locations);
	    regions = _.filter(function (l) {
	      return l.level === 1;
	    }, locations);
	  } else if (location && location.level === 1) {
	    region = location;

	    towns = _.filter(function (l) {
	      return l.level === 2 && l.parent === region.id;
	    }, locations);
	    regions = _.filter(function (l) {
	      return l.level === 1;
	    }, locations);
	  } else {
	    regions = _.filter(function (l) {
	      return l.level === 1;
	    }, locations);
	  }

	  return {
	    subway: subway, district: district, town: town, region: region,
	    subways: subways, districts: districts, towns: towns, regions: regions
	  };
	}

	function getCategoryTree(allCategories, chosenCategory) {
	  var subcategory = undefined,
	      category = undefined,
	      supercategory = undefined;
	  var subcategories = undefined,
	      categories = undefined,
	      supercategories = undefined;

	  if (chosenCategory && chosenCategory.level === 3) {
	    subcategory = chosenCategory;
	    category = _.find({ slug: subcategory.parent }, allCategories);
	    supercategory = _.find({ slug: category.parent }, allCategories);

	    subcategories = _.filter(function (c) {
	      return c.level === 3 && c.parent === category.slug;
	    }, allCategories);
	    categories = _.filter(function (c) {
	      return c.level === 2 && c.parent === supercategory.slug;
	    }, allCategories);
	    supercategories = _.filter(function (c) {
	      return c.level === 1;
	    }, allCategories);
	  } else if (chosenCategory && chosenCategory.level === 2) {
	    category = chosenCategory;
	    supercategory = _.find({ slug: category.parent }, allCategories);

	    subcategories = _.filter(function (c) {
	      return c.level === 3 && c.parent === category.slug;
	    }, allCategories);
	    categories = _.filter(function (c) {
	      return c.level === 2 && c.parent === supercategory.slug;
	    }, allCategories);
	    supercategories = _.filter(function (c) {
	      return c.level === 1;
	    }, allCategories);
	  } else if (chosenCategory && chosenCategory.level === 1) {
	    supercategory = chosenCategory;

	    categories = _.filter(function (c) {
	      return c.level === 2 && c.parent === supercategory.slug;
	    }, allCategories);
	    supercategories = _.filter(function (c) {
	      return c.level === 1;
	    }, allCategories);
	  } else {
	    supercategories = _.filter(function (c) {
	      return c.level === 1;
	    }, allCategories);
	  }

	  return {
	    subcategory: subcategory, category: category, supercategory: supercategory,
	    subcategories: subcategories, categories: categories, supercategories: supercategories
	  };
	}

	function watchLocations($scope, s, locations) {
	  $scope.$watch('s.region', function watch(newVal, oldVal) {
	    if (newVal !== oldVal && s.region) {
	      s.location = s.region;

	      s.towns = _.filter(function (l) {
	        return l.level === 2 && l.parent === s.region.id;
	      }, locations);
	      s.town = undefined;

	      s.districts = [];
	      s.district = undefined;

	      s.subways = [];
	      s.subway = undefined;
	    }
	  });

	  $scope.$watch('s.town', function watch(newVal, oldVal) {
	    if (newVal !== oldVal && s.town) {
	      s.location = s.town;

	      s.districts = _.filter(function (l) {
	        return l.level === 3 && l.parent === s.town.id;
	      }, locations);
	      s.district = undefined;

	      s.subways = [];
	      s.subway = undefined;
	    }
	  });

	  $scope.$watch('s.district', function watch(newVal, oldVal) {
	    if (newVal !== oldVal && s.district) {
	      s.location = s.district;

	      s.subways = _.filter(function (l) {
	        return l.level === 4 && l.parent === s.district.id;
	      }, locations);
	      s.subway = undefined;
	    }
	  });

	  $scope.$watch('s.subway', function watch(newVal, oldVal) {
	    if (newVal !== oldVal && s.subway) s.location = s.subway;
	  });
	}

	function watchCategories($scope, s, allCategories) {
	  $scope.$watch('s.supercategory', function watch(newVal, oldVal) {
	    if (newVal !== oldVal && s.supercategory) {
	      s.chosenCategory = s.supercategory;

	      s.categories = _.filter(function (c) {
	        return c.level === 2 && c.parent === s.supercategory.slug;
	      }, allCategories);
	      s.category = undefined;

	      s.subcategories = [];
	      s.subcategory = undefined;
	    }
	  });

	  $scope.$watch('s.category', function watch(newVal, oldVal) {
	    if (newVal !== oldVal && s.category) {
	      s.chosenCategory = s.category;

	      s.subcategories = _.filter(function (c) {
	        return c.level === 3 && c.parent === s.category.slug;
	      }, allCategories);
	      s.subcategory = undefined;
	    }
	  });

	  $scope.$watch('s.subcategory', function watch(newVal, oldVal) {
	    if (newVal !== oldVal && s.subcategory) s.chosenCategory = s.subcategory;
	  });
	}

	app.controller('AdvertDetailModalCtrl', ['$scope', '$uibModalInstance', 'advert', function AdvertDetailModalCtrl($scope, $uibModalInstance, advert) {
	  var s = $scope.s = {};

	  s.advert = advert;
	  s.close = function () {
	    return $uibModalInstance.dismiss();
	  };

	  $uibModalInstance.rendered.then(function () {

	    $('#myCarousel').carousel({
	      interval: 6000
	    });

	    $(document).on("click", '[id^=carousel-a-selector-]', function () {
	      var id_selector = $(this).attr("id");
	      var id = id_selector.substr(id_selector.length - 1);
	      id = parseInt(id);
	      $('#myCarousel').carousel(id);
	      $('[id^=carousel-selector-]').removeClass('slider-menu-line');
	      $('[id^=carousel-selector-' + id + ']').addClass('slider-menu-line');
	    });

	    $('#myCarousel').bind('slide.bs.carousel', function (e) {
	      var id = $('.item.active').data('slide-number');
	      id = parseInt(id) + 1;
	      $('[id^=carousel-selector-]').removeClass('slider-menu-line');
	      if ($('#carousel-selector-' + id).attr('id')) {
	        $('[id^=carousel-selector-' + id + ']').addClass('slider-menu-line');
	      } else {
	        $('[id^=carousel-selector-0]').addClass('slider-menu-line');
	      }
	    });
	  });
	}]);

	app.controller('ConfirmationModalCtrl', ['$scope', '$uibModalInstance', function ConfirmationModalCtrl($scope, $uibModalInstance) {
	  var s = this;

	  s.yes = function () {
	    return $uibModalInstance.close('yes');
	  };
	  s.cancel = function () {
	    return $uibModalInstance.dismiss();
	  };
	}]);

	//------------------------------------------------------------------------------

	app.controller('AdvertListCtrl', ['$scope', '$uibModal', function AdvertListCtrl($scope, $uibModal) {
	  var s = $scope.s = g.s = {};
	  var d = s.data = g.d = djangoData;

	  d.advertGenders = [{ id: 'boys', name: 'Мальчик' }, { id: 'girls', name: 'Девочка' }];

	  s.advertDisplayModeTemplateId = 'content-cards-grid'; // TODO: Implement saving to a cookie
	  s.selectedSubcategories = [];
	  s.location = undefined;
	  s.chosenCategory = d.chosenCategory;
	  s.advertUserType = '';
	  s.advertGender = '';
	  Object.assign(s, getLocationTree(d.locations, s.location));
	  Object.assign(s, getCategoryTree(d.allCategories, s.chosenCategory));

	  watchLocations($scope, s, d.locations);
	  watchCategories($scope, s, d.allCategories);

	  s.getLocation = function getLocation(locationId) {
	    var loc = _.find(function (l) {
	      return _.includes(l.type, ['subway', 'district']) && l.id === locationId;
	    }, d.locations);
	    return loc && loc.name;
	  };

	  s.advertDetailModal = function advertDetailModal(_advert) {
	    return $uibModal.open({
	      templateUrl: 'advertDetailModalTempl',
	      controller: 'AdvertDetailModalCtrl',
	      resolve: {
	        advert: function advert() {
	          return _advert;
	        }
	      }
	    });
	  };

	  s.advertCategoryFilter = function advertCategoryFilter(advert) {
	    return _.isEmpty(s.selectedSubcategories) || _.includes(advert.category, s.selectedSubcategories);
	  };

	  s.advertUserTypeFilter = function advertUserTypeFilter(advert) {
	    return _.isEmpty(s.advertUserType) || _.includes(advert.user.type, s.advertUserType);
	  };

	  s.advertGenderFilter = function advertGenderFilter(advert) {
	    return _.isEmpty(s.advertGender) || _.includes(advert.gender, s.advertGender);
	  };

	  s.advertLocationFilter = function advertLocationFilter(advert) {
	    if (_.isEmpty(s.location) || !_.isNumber(advert.location)) {
	      // Handle non-specified locations
	      return true;
	    } else {
	      var advertLocation = _.find({ id: advert.location }, d.locations);
	      return advertLocation.lft >= s.location.lft && advertLocation.rght <= s.location.rght;
	    }
	  };

	  s.advertOrder = function advertOrder(advert) {
	    var views = parseInt(advert.views, 10);

	    return {
	      'created_at': new Date(advert.created_at),
	      'price': parseFloat(advert.price),
	      'views': _.isNaN(views) ? 0 : views
	    }[s.advertOrderPred];
	  };
	}]);

	app.controller('AdvertCreateCtrl', ['$scope', function AdvertCreateCtrl($scope) {
	  var s = $scope.s = {};
	  var d = s.data = djangoData;

	  d.advertGenders = [{ id: 'boys', name: 'Мальчик' }, { id: 'girls', name: 'Девочка' }];

	  s.contactName = d.user.first_name; // Pre-fill
	  s.receiveEmailNotifications = true; // Default
	  s.contactPhone = d.contactPhones[0];
	  s.chosenPromoTypes = [];

	  Object.assign(s, getLocationTree(d.locations, s.location));
	  watchLocations($scope, s, d.locations);

	  Object.assign(s, getCategoryTree(d.allCategories, s.chosenCategory));
	  watchCategories($scope, s, d.allCategories);
	}]);

	app.controller('AdvertUpdateCtrl', ['$scope', function AdvertUpdateCtrl($scope) {
	  var s = $scope.s = {};
	  var d = s.data = djangoData;

	  d.advertGenders = [{ id: 'boys', name: 'Мальчик' }, { id: 'girls', name: 'Девочка' }];

	  s.contactName = d.advert.contact_name || d.user.first_name;
	  s.receiveEmailNotifications = d.advert.receive_email_notifications;
	  s.contactPhone = _.find({ id: d.advert.contact_phone }, d.contactPhones);
	  s.location = _.find({ id: d.advert.location }, d.locations);
	  s.chosenCategory = _.find({ slug: d.advert.category }, d.allCategories);

	  Object.assign(s, getLocationTree(d.locations, s.location));
	  watchLocations($scope, s, d.locations);

	  Object.assign(s, getCategoryTree(d.allCategories, s.chosenCategory));
	  watchCategories($scope, s, d.allCategories);

	  s.advertGender = _.find({ id: d.advert.gender }, d.advertGenders);

	  s.title = d.advert.title;
	  s.body = d.advert.body;
	  s.price = d.advert.price;
	}]);

	app.controller('UserUpdateCtrl', ['$scope', function UserUpdateCtrl($scope) {
	  var s = $scope.s = {};
	  var d = s.data = djangoData;
	  var util = $scope.util;

	  d.contactMethods = [{ id: 'email', name: 'Почта' }, { id: 'phone', name: 'Телефон' }];

	  s.contactPhones = d.userContactPhones;
	  s.subscribedToNewsletter = d.user.subscribed_to_newsletter;
	  s.unverifiedContactPhones = [];
	  s.location = _.find({ id: d.user.location }, d.locations);
	  s.contactMethod = _.find({ id: d.user.preferred_contact_method }, d.contactMethods);

	  Object.assign(s, getLocationTree(d.locations, s.location));
	  watchLocations($scope, s, d.locations);

	  s.acceptContactPhone = function acceptContactPhone(phone) {
	    util.remove(phone, s.unverifiedContactPhones);
	    s.contactPhones.push(phone);
	  };
	}]);

	app.controller('UserDeleteCtrl', ['$scope', '$uibModal', function UserDeleteCtrl($scope, $uibModal) {
	  var s = $scope.s = {};

	  s.confirmUserDeletion = function confirmUserDeletion($event, formId) {
	    $event.preventDefault();

	    return $uibModal.open({
	      templateUrl: 'confirmationModalTempl',
	      controller: 'ConfirmationModalCtrl as s'
	    }).result.then(function (res) {
	      if (res === 'yes') document.getElementById(formId).submit();
	    });
	  };
	}]);

	app.controller('UserAdvertsCtrl', ['$scope', '$uibModal', function UserAdvertsCtrl($scope, $uibModal) {
	  var s = $scope.s = {};

	  s.activeAdvertActions = [{ name: 'Архивировать', id: 'archive' }, { name: 'Поднять', id: 'raise' }];
	  s.archivedAdvertActions = [{ name: 'Активировать', id: 'activate' }, { name: 'Поднять', id: 'raise' }];

	  s.confirmAdvertDeletion = function confirmAdvertDeletion(formId) {
	    return $uibModal.open({
	      templateUrl: 'confirmationModalTempl',
	      controller: 'ConfirmationModalCtrl as s'
	    }).result.then(function (res) {
	      if (res === 'yes') document.getElementById(formId).submit();
	    });
	  };
	}]);
	/* WEBPACK VAR INJECTION */}.call(exports, (function() { return this; }())))

/***/ },
/* 1 */
/***/ function(module, exports, __webpack_require__) {

	// style-loader: Adds some css to the DOM by adding a <style> tag

	// load the styles
	var content = __webpack_require__(2);
	if(typeof content === 'string') content = [[module.id, content, '']];
	// add the styles to the DOM
	var update = __webpack_require__(4)(content, {});
	if(content.locals) module.exports = content.locals;
	// Hot Module Replacement
	if(false) {
		// When the styles change, update the <style> tags
		if(!content.locals) {
			module.hot.accept("!!./node_modules/css-loader/index.js!./node_modules/postcss-loader/index.js!./node_modules/less-loader/index.js!./dev-colors.less", function() {
				var newContent = require("!!./node_modules/css-loader/index.js!./node_modules/postcss-loader/index.js!./node_modules/less-loader/index.js!./dev-colors.less");
				if(typeof newContent === 'string') newContent = [[module.id, newContent, '']];
				update(newContent);
			});
		}
		// When the module is disposed, remove the <style> tags
		module.hot.dispose(function() { update(); });
	}

/***/ },
/* 2 */
/***/ function(module, exports, __webpack_require__) {

	exports = module.exports = __webpack_require__(3)();
	// imports


	// module
	exports.push([module.id, ".a {\n  background-color: #ffbfbf !important;\n}\n.b {\n  background-color: #ffe1bf !important;\n}\n.c {\n  background-color: #fbffbf !important;\n}\n.d {\n  background-color: #bfffc8 !important;\n}\n.e {\n  background-color: #bff2ff !important;\n}\n.f {\n  background-color: #bfd0ff !important;\n}\n.g {\n  background-color: #d0bfff !important;\n}\n.h {\n  background-color: #ffbfea !important;\n}\n.i {\n  background-color: #ff8080 !important;\n}\n.j {\n  background-color: #ffc480 !important;\n}\n.k {\n  background-color: #f6ff80 !important;\n}\n.l {\n  background-color: #b2ff80 !important;\n}\n.m {\n  background-color: #80a2ff !important;\n}\n.n {\n  background-color: #a280ff !important;\n}\n.o {\n  background-color: #ff80d5 !important;\n}\n.p {\n  background-color: #ff4040 !important;\n}\n.q {\n  background-color: #40ff59 !important;\n}\n.r {\n  background-color: #40ffbf !important;\n}\n.s {\n  background-color: #40d9ff !important;\n}\n.t {\n  background-color: #7340ff !important;\n}\n.u {\n  background-color: #d940ff !important;\n}\n.v {\n  background-color: #ff8800 !important;\n}\n.w {\n  background-color: #eeff00 !important;\n}\n.x {\n  background-color: #ff00aa !important;\n}\n.y {\n  background-color: #999999 !important;\n}\n.z {\n  background-color: #997373 !important;\n}\n.-borders {\n  border: 1px solid red;\n}\n.-underline {\n  text-decoration: underline;\n}\n", ""]);

	// exports


/***/ },
/* 3 */
/***/ function(module, exports) {

	/*
		MIT License http://www.opensource.org/licenses/mit-license.php
		Author Tobias Koppers @sokra
	*/
	// css base code, injected by the css-loader
	module.exports = function() {
		var list = [];

		// return the list of modules as css string
		list.toString = function toString() {
			var result = [];
			for(var i = 0; i < this.length; i++) {
				var item = this[i];
				if(item[2]) {
					result.push("@media " + item[2] + "{" + item[1] + "}");
				} else {
					result.push(item[1]);
				}
			}
			return result.join("");
		};

		// import a list of modules into the list
		list.i = function(modules, mediaQuery) {
			if(typeof modules === "string")
				modules = [[null, modules, ""]];
			var alreadyImportedModules = {};
			for(var i = 0; i < this.length; i++) {
				var id = this[i][0];
				if(typeof id === "number")
					alreadyImportedModules[id] = true;
			}
			for(i = 0; i < modules.length; i++) {
				var item = modules[i];
				// skip already imported module
				// this implementation is not 100% perfect for weird media query combinations
				//  when a module is imported multiple times with different media queries.
				//  I hope this will never occur (Hey this way we have smaller bundles)
				if(typeof item[0] !== "number" || !alreadyImportedModules[item[0]]) {
					if(mediaQuery && !item[2]) {
						item[2] = mediaQuery;
					} else if(mediaQuery) {
						item[2] = "(" + item[2] + ") and (" + mediaQuery + ")";
					}
					list.push(item);
				}
			}
		};
		return list;
	};


/***/ },
/* 4 */
/***/ function(module, exports, __webpack_require__) {

	/*
		MIT License http://www.opensource.org/licenses/mit-license.php
		Author Tobias Koppers @sokra
	*/
	var stylesInDom = {},
		memoize = function(fn) {
			var memo;
			return function () {
				if (typeof memo === "undefined") memo = fn.apply(this, arguments);
				return memo;
			};
		},
		isOldIE = memoize(function() {
			return /msie [6-9]\b/.test(window.navigator.userAgent.toLowerCase());
		}),
		getHeadElement = memoize(function () {
			return document.head || document.getElementsByTagName("head")[0];
		}),
		singletonElement = null,
		singletonCounter = 0,
		styleElementsInsertedAtTop = [];

	module.exports = function(list, options) {
		if(false) {
			if(typeof document !== "object") throw new Error("The style-loader cannot be used in a non-browser environment");
		}

		options = options || {};
		// Force single-tag solution on IE6-9, which has a hard limit on the # of <style>
		// tags it will allow on a page
		if (typeof options.singleton === "undefined") options.singleton = isOldIE();

		// By default, add <style> tags to the bottom of <head>.
		if (typeof options.insertAt === "undefined") options.insertAt = "bottom";

		var styles = listToStyles(list);
		addStylesToDom(styles, options);

		return function update(newList) {
			var mayRemove = [];
			for(var i = 0; i < styles.length; i++) {
				var item = styles[i];
				var domStyle = stylesInDom[item.id];
				domStyle.refs--;
				mayRemove.push(domStyle);
			}
			if(newList) {
				var newStyles = listToStyles(newList);
				addStylesToDom(newStyles, options);
			}
			for(var i = 0; i < mayRemove.length; i++) {
				var domStyle = mayRemove[i];
				if(domStyle.refs === 0) {
					for(var j = 0; j < domStyle.parts.length; j++)
						domStyle.parts[j]();
					delete stylesInDom[domStyle.id];
				}
			}
		};
	}

	function addStylesToDom(styles, options) {
		for(var i = 0; i < styles.length; i++) {
			var item = styles[i];
			var domStyle = stylesInDom[item.id];
			if(domStyle) {
				domStyle.refs++;
				for(var j = 0; j < domStyle.parts.length; j++) {
					domStyle.parts[j](item.parts[j]);
				}
				for(; j < item.parts.length; j++) {
					domStyle.parts.push(addStyle(item.parts[j], options));
				}
			} else {
				var parts = [];
				for(var j = 0; j < item.parts.length; j++) {
					parts.push(addStyle(item.parts[j], options));
				}
				stylesInDom[item.id] = {id: item.id, refs: 1, parts: parts};
			}
		}
	}

	function listToStyles(list) {
		var styles = [];
		var newStyles = {};
		for(var i = 0; i < list.length; i++) {
			var item = list[i];
			var id = item[0];
			var css = item[1];
			var media = item[2];
			var sourceMap = item[3];
			var part = {css: css, media: media, sourceMap: sourceMap};
			if(!newStyles[id])
				styles.push(newStyles[id] = {id: id, parts: [part]});
			else
				newStyles[id].parts.push(part);
		}
		return styles;
	}

	function insertStyleElement(options, styleElement) {
		var head = getHeadElement();
		var lastStyleElementInsertedAtTop = styleElementsInsertedAtTop[styleElementsInsertedAtTop.length - 1];
		if (options.insertAt === "top") {
			if(!lastStyleElementInsertedAtTop) {
				head.insertBefore(styleElement, head.firstChild);
			} else if(lastStyleElementInsertedAtTop.nextSibling) {
				head.insertBefore(styleElement, lastStyleElementInsertedAtTop.nextSibling);
			} else {
				head.appendChild(styleElement);
			}
			styleElementsInsertedAtTop.push(styleElement);
		} else if (options.insertAt === "bottom") {
			head.appendChild(styleElement);
		} else {
			throw new Error("Invalid value for parameter 'insertAt'. Must be 'top' or 'bottom'.");
		}
	}

	function removeStyleElement(styleElement) {
		styleElement.parentNode.removeChild(styleElement);
		var idx = styleElementsInsertedAtTop.indexOf(styleElement);
		if(idx >= 0) {
			styleElementsInsertedAtTop.splice(idx, 1);
		}
	}

	function createStyleElement(options) {
		var styleElement = document.createElement("style");
		styleElement.type = "text/css";
		insertStyleElement(options, styleElement);
		return styleElement;
	}

	function createLinkElement(options) {
		var linkElement = document.createElement("link");
		linkElement.rel = "stylesheet";
		insertStyleElement(options, linkElement);
		return linkElement;
	}

	function addStyle(obj, options) {
		var styleElement, update, remove;

		if (options.singleton) {
			var styleIndex = singletonCounter++;
			styleElement = singletonElement || (singletonElement = createStyleElement(options));
			update = applyToSingletonTag.bind(null, styleElement, styleIndex, false);
			remove = applyToSingletonTag.bind(null, styleElement, styleIndex, true);
		} else if(obj.sourceMap &&
			typeof URL === "function" &&
			typeof URL.createObjectURL === "function" &&
			typeof URL.revokeObjectURL === "function" &&
			typeof Blob === "function" &&
			typeof btoa === "function") {
			styleElement = createLinkElement(options);
			update = updateLink.bind(null, styleElement);
			remove = function() {
				removeStyleElement(styleElement);
				if(styleElement.href)
					URL.revokeObjectURL(styleElement.href);
			};
		} else {
			styleElement = createStyleElement(options);
			update = applyToTag.bind(null, styleElement);
			remove = function() {
				removeStyleElement(styleElement);
			};
		}

		update(obj);

		return function updateStyle(newObj) {
			if(newObj) {
				if(newObj.css === obj.css && newObj.media === obj.media && newObj.sourceMap === obj.sourceMap)
					return;
				update(obj = newObj);
			} else {
				remove();
			}
		};
	}

	var replaceText = (function () {
		var textStore = [];

		return function (index, replacement) {
			textStore[index] = replacement;
			return textStore.filter(Boolean).join('\n');
		};
	})();

	function applyToSingletonTag(styleElement, index, remove, obj) {
		var css = remove ? "" : obj.css;

		if (styleElement.styleSheet) {
			styleElement.styleSheet.cssText = replaceText(index, css);
		} else {
			var cssNode = document.createTextNode(css);
			var childNodes = styleElement.childNodes;
			if (childNodes[index]) styleElement.removeChild(childNodes[index]);
			if (childNodes.length) {
				styleElement.insertBefore(cssNode, childNodes[index]);
			} else {
				styleElement.appendChild(cssNode);
			}
		}
	}

	function applyToTag(styleElement, obj) {
		var css = obj.css;
		var media = obj.media;
		var sourceMap = obj.sourceMap;

		if(media) {
			styleElement.setAttribute("media", media)
		}

		if(styleElement.styleSheet) {
			styleElement.styleSheet.cssText = css;
		} else {
			while(styleElement.firstChild) {
				styleElement.removeChild(styleElement.firstChild);
			}
			styleElement.appendChild(document.createTextNode(css));
		}
	}

	function updateLink(linkElement, obj) {
		var css = obj.css;
		var media = obj.media;
		var sourceMap = obj.sourceMap;

		if(sourceMap) {
			// http://stackoverflow.com/a/26603875
			css += "\n/*# sourceMappingURL=data:application/json;base64," + btoa(unescape(encodeURIComponent(JSON.stringify(sourceMap)))) + " */";
		}

		var blob = new Blob([css], { type: "text/css" });

		var oldSrc = linkElement.href;

		linkElement.href = URL.createObjectURL(blob);

		if(oldSrc)
			URL.revokeObjectURL(oldSrc);
	}


/***/ },
/* 5 */
/***/ function(module, exports, __webpack_require__) {

	// style-loader: Adds some css to the DOM by adding a <style> tag

	// load the styles
	var content = __webpack_require__(6);
	if(typeof content === 'string') content = [[module.id, content, '']];
	// add the styles to the DOM
	var update = __webpack_require__(4)(content, {});
	if(content.locals) module.exports = content.locals;
	// Hot Module Replacement
	if(false) {
		// When the styles change, update the <style> tags
		if(!content.locals) {
			module.hot.accept("!!./node_modules/css-loader/index.js!./node_modules/postcss-loader/index.js!./node_modules/less-loader/index.js!./more-styles.less", function() {
				var newContent = require("!!./node_modules/css-loader/index.js!./node_modules/postcss-loader/index.js!./node_modules/less-loader/index.js!./more-styles.less");
				if(typeof newContent === 'string') newContent = [[module.id, newContent, '']];
				update(newContent);
			});
		}
		// When the module is disposed, remove the <style> tags
		module.hot.dispose(function() { update(); });
	}

/***/ },
/* 6 */
/***/ function(module, exports, __webpack_require__) {

	exports = module.exports = __webpack_require__(3)();
	// imports


	// module
	exports.push([module.id, ".-no-select {\n  -webkit-user-select: none;\n     -moz-user-select: none;\n      -ms-user-select: none;\n          user-select: none;\n}\n.-advert-placement .-categories .-cat-column {\n  height: 340px;\n  overflow-y: auto;\n}\n", ""]);

	// exports


/***/ }
/******/ ]);