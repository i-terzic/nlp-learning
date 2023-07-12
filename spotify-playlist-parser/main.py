import csv

def findDuplicates(file_name):
    """A function that finds duplicate song tracks among playlists."""
    print('Finding duplicate tracks in %s...' % file_name)

    with open(file_name, newline="") as csvfile:
        tracks = list(csv.reader(csvfile, delimiter=","))
        track_names = {}

        # Track name,Artist name,Album,Playlist name,Type,ISRC

        for track in tracks:
            name = track[0]
            if name in track_names:
                track_names[name] += 1
            else:
                track_names[name] = 1

        dups = []
        for key, value in track_names.items():
            if value > 1:
                dups.append((key, value))
        if len(dups) > 0:
            print("Found %d duplicates. Track names saved to dup.txt" % len(dups))
        else:
            print("No duplicate tracks found!")
        
        with open("dups.txt", "w") as f:
            for val in dups:
                f.write("[%s] %s\n" % (val[0], val[1]))
   



def main():
    file_name = "./spotify-playlist-parser/data/spotify_data.csv"

    findDuplicates(file_name=file_name)


if __name__ == "__main__":
    main()
