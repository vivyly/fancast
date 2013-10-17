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

angular.module("casting.app.resource",[]).
    controller("CastingController", ["$scope","$http", 
        function($scope, $http){
            //get all chracters
            $scope.characters = [];
            $http.get('/api/characters/EyA9Ld9U7jknsdqioUWa4X').success(
                function(data){
                    $scope.characters = data.results;
            })

}]);




//console.log('in script');
//angular.module("casting.app.resource", [])
//    .factory("castingFactory", ["$http", function($http){
//    var castingFactory = {};
//    castingFactory.getCharacters = function(id){
//        return $http.get("/api/characters/"+id);  
//    };
//    
//    castingFactory.getActors = function(id){
//        return $http.get("/api/actors/"+id);
//    };
//
//    return castingFactory
//}])
//    .controller("castingController", 
//        ["$scope", "castingFactory", function($scope, castingFactory){
//        $scope.characters;
//        console.log('in controller');
//        getCharacters();
//        function getCharacters(){
//            castingFactory.getCharacters()
//            .success(function(data){
//                $scope.characters = data.results;
//            });
//        }
//        $scope.getActors = function(id){
//            var character;
//            for (var i = 0; i < $scope.characters.length; i++){
//                var currentChar = $scope.characters[i];
//                if (currentChar.slug === id){
//                    castingFactory.getActors()
//                    .success(function(data){
//                        currentChar.actors = data.results;
//                    });
//                }
//            }
//        }
//}]);


