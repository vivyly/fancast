//come back to doing this later
//angular.module("casting.api", ["ngResource"]).
//    factory("Character", function($resource){
//        return $resource("/api/characters/:projectId",{
//                         projectId:"EyA9Ld9U7jknsdqioUWa4X"},{
//                         "query":{method:"GET", format:"json", isArray:true,
//                         transformResponse:[function(data, headersGetter){
//                            console.log(data);
//                         }]}
//                         });
//    });
//
//
//angular.module("casting.app.resource", ["casting.api"]).
//    controller("CastingController", function(
//                                    Character, $routeParams, $scope){
//        console.log("params:"+$routeParams);
//        $scope.characters = Character.query();
//        console.log("characters:"+$scope.characters);
//    })

//angular.module("casting.app.resource",[]).
//    controller("CastingController", ["$scope","$http", 
//        function($scope, $http){
//            //get all chracters
//            $scope.characters = [];
//            $http.get('/api/characters/EyA9Ld9U7jknsdqioUWa4X').success(
//                function(data){
//                    $scope.characters = data.results;
//            })
//
//}]);



var castingApp = angular.module('casting.app.resource', []);

castingApp.factory("castingFactory", ["$http", function($http){
    var apiBase = "/api/";
    var castingFactory = {};
    castingFactory.getCharacters = function(id){
        return $http.get(apiBase+'characters/EyA9Ld9U7jknsdqioUWa4X');
    };
    return castingFactory;
}]);
    
castingApp.controller("CastingController", ["$scope", "castingFactory",
    function($scope, castingFactory){
        $scope.characters = [];
        getCharacters();
        function getCharacters(){
            castingFactory.getCharacters()
                .success(function(result){
                    $scope.characters = result.results;
                    console.dir($scope.characters);
                });
        }
}]);


