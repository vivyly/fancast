var castingApp = angular.module('casting.app.resource', ['ngResource']);

castingApp.factory("CastingFactory", 
        ["$http", '$resource', function($http, $resource){

    var apiBase = "/api/";
    var CastingFactory = {};
    CastingFactory.getCharacters = function(id){
        return $http.get(apiBase+'characters/'+id);
    };
    CastingFactory.vote = function(prospect_id, vote_status){
        data = {"vote_status":vote_status?1:0};
        return $http({url: apiBase+'vote/'+prospect_id,
                      method: 'POST',
                      data:data});
    };
    return CastingFactory;
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
}])
.factory("CharacterHandler", ["$rootScope", function($rootScope){
    $rootScope.characters = [];
    var CharacterHandler = {};    
    CharacterHandler.setAllCharacters = function(result){
        $rootScope.characters = result; 
    };
    CharacterHandler.updateCharacter = function(character_id, result){
        for(var i = 0; i < $rootScope.characters.length; i++){
            var currentCharacter = $rootScope.characters[i];
            if (currentCharacter.slug === character_id){
                currentCharacter.prospects = result;
            }
        }
    };
    return CharacterHandler;
}])
.factory("ActorResource", ["$resource", "CharacterHandler",
        function($resource, CharacterHandler){
    var addCharacterId = '';
    return $resource('/add/actor/',{},{
        create:{method:'POST', isArray: true,
                transformResponse:function(data, header){
                    var response = JSON.parse(data);
                    return response;
                }
        },
    });
}]);

    
castingApp.controller("CastingController", 
        ["$scope", "CastingFactory", "Constants", "CharacterHandler",
    function($scope, CastingFactory, Constants, CharacterHandler){
        $scope.projectId = Constants.get('projectId');
        getCharacters();
        function getCharacters(){
            CastingFactory.getCharacters($scope.projectId)
                .success(function(result){
                    CharacterHandler.setAllCharacters(result.results);
                });
        }
    $scope.vote = function(character_id, prospect_id, vote_status){
        CastingFactory.vote(prospect_id, vote_status)
            .success(function(result){
                CharacterHandler.updateCharacter(character_id, result);
            });
    };
    $scope.openDialog = function(character_id){
        CharacterHandler.addCharacterId = character_id;
        Overlay.show();
    };
}]);

castingApp.controller('CastingOverlay',
    ['$scope', 'ActorResource','CharacterHandler',
    function($scope, ActorResource, CharacterHandler){
    $scope.closeDialog = function(){
        Overlay.close();
    };
    $scope.add = function(input){
        var character_id = CharacterHandler.addCharacterId;
        input['character_id'] = character_id;
        ActorResource.create(input, function(result){
            CharacterHandler.updateCharacter(character_id, result);
            $scope.closeDialog();
        });
    };

}]);
