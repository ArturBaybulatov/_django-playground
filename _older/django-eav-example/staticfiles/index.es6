import './style.less'
import './dev-colors.less'

global.g = global

const $$ = g.$$ = myUtil

const MONTHS = ['01','02','03','04','05','06','07','08','09','10','11','12']

g.DEBUG = false

const app = angular.module('app', ['ui.bootstrap', 'ui.select', 'checklist-model', 'ui.bootstrap-slider'])


app.config(['$interpolateProvider', '$httpProvider', function($interpolateProvider, $httpProvider) {
  $interpolateProvider.startSymbol('{(')
  $interpolateProvider.endSymbol(')}')
  
  $httpProvider.defaults.xsrfCookieName = 'csrftoken'
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken'
}])




app.service('util', function util() {
  const s = this
  
  s.remove = function remove(item, coll) {
    $$.splice(1, coll.indexOf(item), coll)
  }
})





app.run(['$rootScope', 'util', '$timeout', '$http', function run(s, util, $timeout, $http) {
  s._ = _
  s.$$ = $$
  s.Math = Math
  s.util = util
  
  
  global.$http = $http // Debug
  
  
  //$timeout(function() {
  //  $('.-icheck.-icheck-default input[type="checkbox"]').icheck({checkboxClass: 'icheckbox_square'})
  //  $('.-icheck.-icheck-blue input[type="checkbox"]').icheck({checkboxClass: 'icheckbox_square-blue'})
  //  
  //  $('.-icheck input[type="radio"].-icheck-default').icheck({radioClass: 'iradio_square'})
  //  $('.-icheck input[type="radio"].-icheck-white').icheck({radioClass: 'iradio_square'})
  //  $('.-icheck input[type="radio"].-icheck-violet').icheck({radioClass: 'iradio_square-purple'})
  //  $('.-icheck input[type="radio"].-icheck-red').icheck({radioClass: 'iradio_square-red'})
  //  $('.-icheck input[type="radio"].-icheck-green').icheck({radioClass: 'iradio_square-green'})
  //  $('.-icheck input[type="radio"].-icheck-gray').icheck({radioClass: 'iradio_square-grey'})
  //  $('.-icheck input[type="radio"].-icheck-blue').icheck({radioClass: 'iradio_square-blue'})
  //  $('.-icheck input[type="radio"].-icheck-yellow').icheck({radioClass: 'iradio_square-yellow'})
  //  $('.-icheck input[type="radio"].-icheck-cyan').icheck({radioClass: 'iradio_square'})
  //})
}])






function getLocationTree(locations, location) {
  let subway, district, town, region
  let subways, districts, towns, regions
  
  
  if (location && location.level === 4) {
    subway = location
    district = _.find({id: subway.parent}, locations)
    town = _.find({id: district.parent}, locations)
    region = _.find({id: town.parent}, locations)
    
    subways = _.filter(l => l.level === 4 && l.parent === district.id, locations)
    districts = _.filter(l => l.level === 3 && l.parent === town.id, locations)
    towns = _.filter(l => l.level === 2 && l.parent === region.id, locations)
    regions = _.filter(l => l.level === 1, locations)
  } else if (location && location.level === 3) {
    district = location
    town = _.find({id: district.parent}, locations)
    region = _.find({id: town.parent}, locations)
    
    subways = _.filter(l => l.level === 4 && l.parent === district.id, locations)
    districts = _.filter(l => l.level === 3 && l.parent === town.id, locations)
    towns = _.filter(l => l.level === 2 && l.parent === region.id, locations)
    regions = _.filter(l => l.level === 1, locations)
  } else if (location && location.level === 2) {
    town = location
    region = _.find({id: town.parent}, locations)
    
    districts = _.filter(l => l.level === 3 && l.parent === town.id, locations)
    towns = _.filter(l => l.level === 2 && l.parent === region.id, locations)
    regions = _.filter(l => l.level === 1, locations)
  } else if (location && location.level === 1) {
    region = location
    
    towns = _.filter(l => l.level === 2 && l.parent === region.id, locations)
    regions = _.filter(l => l.level === 1, locations)
  } else {
    regions = _.filter(l => l.level === 1, locations)
  }
  
  
  return {
    subway, district, town, region,
    subways, districts, towns, regions,
  }
}











function getCategoryTree(allCategories, chosenCategory) {
  let subcategory, category, supercategory
  let subcategories, categories, supercategories
  
  
  if (chosenCategory && chosenCategory.level === 3) {
    subcategory = chosenCategory
    category = _.find({slug: subcategory.parent}, allCategories)
    supercategory = _.find({slug: category.parent}, allCategories)
    
    subcategories = _.filter(c => c.level === 3 && c.parent === category.slug, allCategories)
    categories = _.filter(c => c.level === 2 && c.parent === supercategory.slug, allCategories)
    supercategories = _.filter(c => c.level === 1, allCategories)
  } else if (chosenCategory && chosenCategory.level === 2) {
    category = chosenCategory
    supercategory = _.find({slug: category.parent}, allCategories)
    
    subcategories = _.filter(c => c.level === 3 && c.parent === category.slug, allCategories)
    categories = _.filter(c => c.level === 2 && c.parent === supercategory.slug, allCategories)
    supercategories = _.filter(c => c.level === 1, allCategories)
  } else if (chosenCategory && chosenCategory.level === 1) {
    supercategory = chosenCategory
    
    categories = _.filter(c => c.level === 2 && c.parent === supercategory.slug, allCategories)
    supercategories = _.filter(c => c.level === 1, allCategories)
  } else {
    supercategories = _.filter(c => c.level === 1, allCategories)
  }
  
  
  return {
    subcategory, category, supercategory,
    subcategories, categories, supercategories,
  }
}













function watchLocations($scope, s, locations) {
  $scope.$watch('s.region', function watch(newVal, oldVal) {
    if (newVal !== oldVal && s.region) {
      s.location = s.region
      
      s.towns = _.filter(l => l.level === 2 && l.parent === s.region.id, locations)
      s.town = undefined
      
      s.districts = []
      s.district = undefined
      
      s.subways = []
      s.subway = undefined
    }
  })
  
  $scope.$watch('s.town', function watch(newVal, oldVal) {
    if (newVal !== oldVal && s.town) {
      s.location = s.town
      
      s.districts = _.filter(l => l.level === 3 && l.parent === s.town.id, locations)
      s.district = undefined
      
      s.subways = []
      s.subway = undefined
    }
  })
  
  $scope.$watch('s.district', function watch(newVal, oldVal) {
    if (newVal !== oldVal && s.district) {
      s.location = s.district
      
      s.subways = _.filter(l => l.level === 4 && l.parent === s.district.id, locations)
      s.subway = undefined
    }
  })
  
  $scope.$watch('s.subway', function watch(newVal, oldVal) {
    if (newVal !== oldVal && s.subway)
      s.location = s.subway
  })
}










function watchCategories($scope, s, allCategories) {
  $scope.$watch('s.supercategory', function watch(newVal, oldVal) {
    if (newVal !== oldVal && s.supercategory) {
      s.chosenCategory = s.supercategory
      
      s.categories = _.filter(c => c.level === 2 && c.parent === s.supercategory.slug, allCategories)
      s.category = undefined
      
      s.subcategories = []
      s.subcategory = undefined
    }
  })
  
  $scope.$watch('s.category', function watch(newVal, oldVal) {
    if (newVal !== oldVal && s.category) {
      s.chosenCategory = s.category
      
      s.subcategories = _.filter(c => c.level === 3 && c.parent === s.category.slug, allCategories)
      s.subcategory = undefined
    }
  })
  
  $scope.$watch('s.subcategory', function watch(newVal, oldVal) {
    if (newVal !== oldVal && s.subcategory)
      s.chosenCategory = s.subcategory
  })
}








app.controller('AdvertDetailModalCtrl', [
  '$scope', '$uibModalInstance', 'advert',
  
  function AdvertDetailModalCtrl($scope, $uibModalInstance, advert) {
    const s = $scope.s = {}
    
    s.advert = advert
    s.close = () => $uibModalInstance.dismiss()


    $uibModalInstance.rendered.then(function(){

 $('#myCarousel').carousel({
  interval: 6000
  });

  $(document).on("click", '[id^=carousel-a-selector-]', function(){
  var id_selector = $(this).attr("id");
  var id = id_selector.substr(id_selector.length -1);
  id = parseInt(id);
  $('#myCarousel').carousel(id);
  $('[id^=carousel-selector-]').removeClass('slider-menu-line');
  $('[id^=carousel-selector-'+id+']').addClass('slider-menu-line');
  });


      $('#myCarousel').bind('slide.bs.carousel', function (e) {
      var id = $('.item.active').data('slide-number');
      id = parseInt(id)+1;
      $('[id^=carousel-selector-]').removeClass('slider-menu-line');
      if( $('#carousel-selector-'+ id).attr('id')){
      	$('[id^=carousel-selector-' + id + ']').addClass('slider-menu-line');
      }
      else{
      	$('[id^=carousel-selector-0]').addClass('slider-menu-line');
      }
      
      });
  
    });
  }]);





app.controller('ConfirmationModalCtrl', [
  '$scope', '$uibModalInstance',
  
  function ConfirmationModalCtrl($scope, $uibModalInstance) {
    const s = this
    
    s.yes = () => $uibModalInstance.close('yes')
    s.cancel = () => $uibModalInstance.dismiss()
  },
])



















//------------------------------------------------------------------------------





















app.controller('AdvertListCtrl', ['$scope', '$uibModal', function AdvertListCtrl($scope, $uibModal) {
  const s = $scope.s = g.s = {}
  const d = s.data = g.d = djangoData
  
  
  d.advertGenders = [{id: 'boys', name: 'Мальчик'}, {id: 'girls', name: 'Девочка'}]
  
  
  s.advertDisplayModeTemplateId = 'content-cards-grid' // TODO: Implement saving to a cookie
  s.selectedSubcategories = []
  s.location = undefined
  s.chosenCategory = d.chosenCategory
  s.advertUserType = ''
  s.advertGender = ''
  Object.assign(s, getLocationTree(d.locations, s.location))
  Object.assign(s, getCategoryTree(d.allCategories, s.chosenCategory))
  
}])
