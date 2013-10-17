function VoteController($scope){
    $scope.actors = [
    {
        name:"byung hun lee",
        image:"",
        upvote:false,
        downvote:false,
        starttotal:5
    },
    {
        name:"Lee Pace",
        image:"",
        upvote:false,
        downvote:false,
        starttotal:4
    },
    {
        name:"Joseph Gordon Levitt",
        image:"",
        upvote:false,
        downvote:false,
        starttotal:10
    },
    {
        name:"Adrien Brody",
        image:"",
        upvote:false,
        downvote:false,
        starttotal:4
    },
    {
        name:"Keanu Reeves",
        image:"",
        upvote:false,
        downvote:false,
        starttotal:2
    },
    {
        name:"Ben Schwartz",
        image:"",
        upvote:false,
        downvote:false,
        starttotal:0
    },
    ];

    $scope.toggleUpvote = function(s){
        s.upvote = !s.upvote;
    }

    $scope.toggleDownvote = function(s){
        s.downvote = !s.downvote;
    }

    $scope.total = function(s){
        return s.starttotal + (s.upvote - s.downvote)
    }

}
