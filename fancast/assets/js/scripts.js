var castingApp = angular.module('casting.app.resource', []);

castingApp.factory("castingFactory", ["$http", function($http){
    var apiBase = "/api/";
    var castingFactory = {};
    castingFactory.getCharacters = function(id){
        return $http.get(apiBase+'characters/'+id);
    };
    castingFactory.vote = function(prospect_id, vote_status){
        data = {"vote_status":vote_status?1:0};
        return $http({url:apiBase+'vote/'+prospect_id,
                      method: 'POST',
                      data:data});
    };
    return castingFactory;
}])
.factory("Constants", ["DjangoConstants", 
                        function(DjangoConstants){
    var constants = {
        sessionID: "sessionID",
        projectId: "projectId"
    };
    angular.extend(constants, DjangoConstants);
    return{
        get: function(key){
            return constants[key];
        }
    }
}]);

    
castingApp.controller("CastingController", 
        ["$scope", "castingFactory", "Constants",
    function($scope, castingFactory, Constants){
        $scope.characters = [];
        $scope.projectId = Constants.get('projectId');
        getCharacters();
        function getCharacters(){
            castingFactory.getCharacters($scope.projectId)
                .success(function(result){
                    $scope.characters = result.results;
                });
        }

    $scope.vote = function(character_id, prospect_id, vote_status){
        castingFactory.vote(prospect_id, vote_status)
            .success(function(result){
                for(var i = 0; i < $scope.characters.length; i++){
                    var currentCharacter = $scope.characters[i];
                    if (currentCharacter.slug === character_id){
                        currentCharacter.prospects = result;
                    }
                }
            });
    };
}]);


