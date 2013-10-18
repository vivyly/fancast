var castingApp = angular.module('casting.app.resource', []);

castingApp.factory("castingFactory", ["$http", function($http){
    var apiBase = "/api/";
    var castingFactory = {};
    castingFactory.getCharacters = function(id){
        return $http.get(apiBase+'characters/EyA9Ld9U7jknsdqioUWa4X');
    };
    castingFactory.vote = function(prospect_id, vote_status){
        data = {"vote_status":vote_status?1:0};
        return $http({url:apiBase+'vote/'+prospect_id,
                      method: 'POST',
                      data:data});
    };
    return castingFactory;
}]);

castingApp.factory("SessionIdService", function(){
    var sessionID = '';
    var sessionFactory = {};
    sessionFactory.getSessionId = function(){
        if (sessionID == '' || sessionID == null)
            sessionID = localStorage.getItem("sessionid");
        console.log("sessionID: " + sessionID);
        return sessionID;
    };
    return sessionFactory;
});
    
castingApp.controller("CastingController", 
        ["$scope", "castingFactory", "SessionIdService",
    function($scope, castingFactory, SessionIdService){
        $scope.characters = [];
        getCharacters();
        getSession(); 
        function getCharacters(){
            castingFactory.getCharacters()
                .success(function(result){
                    $scope.characters = result.results;
                    console.dir($scope.characters);
                });
        }

        function getSession(){
            SessionIdService.getSessionId();
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


