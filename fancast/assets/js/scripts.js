var castingApp = angular.module('casting.app.resource', ['ngResource']);

castingApp.factory("CastingFactory", 
        ["$http", '$resource', function($http, $resource){

    var apiBase = "/api/";
    var CastingFactory = {};
    CastingFactory.getCharacters = function(id){
        return $http.get(apiBase+'characters/'+id);
    };
    CastingFactory.vote = function(prospect_id, vote_status){
        data = {"vote_status":vote_status};
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
    CharacterHandler.addCharacter = function(new_character){
        $rootScope.characters.push(new_character);
    };
    return CharacterHandler;
}])
.factory("ActorResource", ["$resource", function($resource){
    return $resource('/add/actor',{},{
        create:{method:'POST', isArray: true,
                transformResponse:function(data, header){
                    var response = JSON.parse(data);
                    return response;
                }
        }
    });
}])
.factory("CharacterResource",['$resource', function($resource){
    return $resource('/add/character', {}, {
        create:{method:'POST', isArray: true,
                transformResponse:function(data, header){
                    var response = JSON.parse(data);
                    return response;
                }
        }
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
    $scope.openDialog = function(template, character_id){
        var template_dom = $('#'+template);
        $('#dialog').append(template_dom);
        if (character_id)
            CharacterHandler.addCharacterId = character_id;
        Overlay.show('#'+template);
    };
}]);

castingApp.controller('CastingOverlay',
    ['$scope', 'Constants', 'ActorResource',
                'CharacterHandler', 'CharacterResource',
    function($scope, Constants, ActorResource,
                                CharacterHandler, CharacterResource){
    $scope.closeDialog = function(){
        Overlay.close();
    };
    $scope.addActor = function(input){
        var character_id = CharacterHandler.addCharacterId;
        input['character_id'] = character_id;
        ActorResource.create(input, function(result){
            CharacterHandler.updateCharacter(character_id, result);
            $scope.closeDialog();
            $scope.cleanOverlay('addActorForm');
        });
    };
    $scope.addCharacter = function(input){
        input['project_id'] = Constants.get('projectId');
        CharacterResource.create(input, function(results){
            for (var i = 0; i < results.length; i++)
                CharacterHandler.addCharacter(results[i]);
            $scope.closeDialog();
            $scope.cleanOverlay('addCharacterForm');
        });
    };
    $scope.cleanOverlay = function(form_id){
       $("#"+form_id+" input").each(function(){
            $(this).val('');
       }); 
    };

}]);
